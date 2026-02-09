terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}


#STEP 1 – CloudWatch Log Groups (Terraform)
#cloudwatchlog groups for lambda
resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/dh-observability"
  retention_in_days = 30
}

resource "aws_cloudwatch_log_group" "health_logs" {
  name              = "/aws/health/dedicated-hosts"
  retention_in_days = 30
}

resource "aws_cloudwatch_log_group" "ram_logs" {
  name              = "/aws/ram/dedicated-hosts"
  retention_in_days = 30
}

#STEP 2 – S3 Bucket for CloudTrail
#S3 bucket
resource "aws_s3_bucket" "cloudtrail_bucket" {
  bucket = "dh-observability-cloudtrail-logs-${var.region}"
}

resource "aws_s3_bucket_policy" "cloudtrail_policy" {
  bucket = aws_s3_bucket.cloudtrail_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action = [
          "s3:GetBucketAcl",
          "s3:PutObject"
        ]
        Resource = [
          aws_s3_bucket.cloudtrail_bucket.arn,
          "${aws_s3_bucket.cloudtrail_bucket.arn}/*"
        ]
        Condition = {
          StringEquals = {
            "s3:x-amz-acl" = "bucket-owner-full-control"
          }
        }
      }
    ]
  })
}


#STEP 3 – CloudTrail CloudWatch Role
#cloudtrail cloudwatch role
resource "aws_iam_role" "cloudtrail_logs_role" {
  name = "dh-cloudtrail-logs-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "cloudtrail_logs_policy" {
  role = aws_iam_role.cloudtrail_logs_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}


#STEP 4 – Organization CloudTrail
#organizational cloudtrail
resource "aws_cloudtrail" "org_trail" {
  name                          = "org-dedicated-host-trail"
  is_organization_trail         = true
  s3_bucket_name                = aws_s3_bucket.cloudtrail_bucket.id
  cloud_watch_logs_group_arn    = "${aws_cloudwatch_log_group.lambda_logs.arn}:*"
  cloud_watch_logs_role_arn     = aws_iam_role.cloudtrail_logs_role.arn
  include_global_service_events = true
  enable_logging                = true
}



#STEP 5 – EventBridge Rules
#EC2 API Events Rule
resource "aws_cloudwatch_event_rule" "ec2_api_events" {
  name = "dh-ec2-api-events"

  event_pattern = jsonencode({
    source = ["aws.ec2"]
    detail-type = ["AWS API Call via CloudTrail"]
    detail = {
      eventSource = ["ec2.amazonaws.com"]
      eventName = [
        "AllocateHosts",
        "ReleaseHosts",
        "RunInstances",
        "TerminateInstances",
        "StartInstances",
        "StopInstances"
      ]
    }
  })
}

# AWS RAM API Events Rule
resource "aws_cloudwatch_event_rule" "ram_api_events" {
  name = "dh-ram-api-events"

  event_pattern = jsonencode({
    source = ["aws.ram"]
    detail-type = ["AWS API Call via CloudTrail"]
    detail = {
      eventSource = ["ram.amazonaws.com"]
    }
  })
}

#AWS Health Events Rule
resource "aws_cloudwatch_event_rule" "aws_health_events" {
  name = "dh-aws-health-events"

  event_pattern = jsonencode({
    source = ["aws.health"]
  })
}


#STEP 6 – IAM Role for Observability Lambda
#lambda=Create IAM Role (Trust Policy)
resource "aws_iam_role" "observability_lambda_role" {
  name = "dh-observability-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "observability_lambda_policy" {
  name = "dh-observability-lambda-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [

      # --------------------------------
      # EC2 Read-only (Dedicated Hosts + Instances)
      # --------------------------------
      {
        Effect = "Allow"
        Action = [
          "ec2:DescribeHosts",
          "ec2:DescribeInstances",
          "ec2:DescribeTags"
        ]
        Resource = "*"
      },

      # --------------------------------
      # AWS Health events
      # --------------------------------
      {
        Effect = "Allow"
        Action = [
          "health:DescribeEvents",
          "health:DescribeEventDetails",
          "health:DescribeAffectedEntities"
        ]
        Resource = "*"
      },

      # --------------------------------
      # Publish custom metrics
      # --------------------------------
      {
        Effect = "Allow"
        Action = "cloudwatch:PutMetricData"
        Resource = "*"
      },

      # --------------------------------
      # CloudWatch Logs
      # --------------------------------
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      },

      # --------------------------------
      # Cross-account access (App accounts)
      # --------------------------------
      {
        Effect = "Allow"
        Action = "sts:AssumeRole"
        Resource = "arn:aws:iam::*:role/dh-observability-ec2-read"
      }
    ]
  })
}



#attach policy to role
resource "aws_iam_role_policy_attachment" "lambda_policy_attach" {
  role       = aws_iam_role.observability_lambda_role.name
  policy_arn = aws_iam_policy.observability_lambda_policy.arn
}

#STEP 7- Create the Lambda Function (CCOE account)
#lambda function create
#create dummy code first  =Terraform cannot create a Lambda without code.
# def lambda_handler(event, context):
#     print("Event received:")
#     print(event)
#     return {"status": "ok"}

#zip it..
#zip lambda.zip handler.py


#lambda
resource "aws_lambda_function" "observability_lambda" {
  function_name = "dh-observability"

  role    = aws_iam_role.observability_lambda_role.arn
  runtime = "python3.11"
  handler = "handler.lambda_handler"

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

  timeout     = 300
  memory_size = 512

  environment {
    variables = {
      METRIC_NAMESPACE = "DedicatedHost/Observability"
    }
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_policy_attach,
    aws_cloudwatch_log_group.lambda_logs
  ]
}


#STEP 8
##EventBridge does NOT know where to send events, Lambda does NOT allow EventBridge to invoke it
# EventBridge → Lambda Targets
#EC2 API events → Lambda
resource "aws_cloudwatch_event_target" "ec2_to_lambda" {
  rule      = aws_cloudwatch_event_rule.ec2_api_events.name
  target_id = "ec2-events"
  arn       = aws_lambda_function.observability_lambda.arn
}
#RAM API events → Lambda
resource "aws_cloudwatch_event_target" "ram_to_lambda" {
  rule      = aws_cloudwatch_event_rule.ram_api_events.name
  target_id = "ram-events"
  arn       = aws_lambda_function.observability_lambda.arn
}
#AWS Health events → Lambda
resource "aws_cloudwatch_event_target" "health_to_lambda" {
  rule      = aws_cloudwatch_event_rule.aws_health_events.name
  target_id = "health-events"
  arn       = aws_lambda_function.observability_lambda.arn
}


#Allow EventBridge to Invoke Lambda
#Permission for EC2 rule
resource "aws_lambda_permission" "allow_ec2_eventbridge" {
  statement_id  = "AllowExecutionFromEC2EventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.observability_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ec2_api_events.arn
}


#Permission for RAM rule
resource "aws_lambda_permission" "allow_ram_eventbridge" {
  statement_id  = "AllowExecutionFromRAMEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.observability_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ram_api_events.arn
}

#Permission for AWS Health rule
resource "aws_lambda_permission" "allow_health_eventbridge" {
  statement_id  = "AllowExecutionFromHealthEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.observability_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.aws_health_events.arn
}

#STEP 9 
#replace dummy lambda code with original one = handler.py , zip and redeploy zip lambda.zip handler.py
# import boto3
# import os
# import datetime
# import json

# ec2 = boto3.client("ec2")
# cloudwatch = boto3.client("cloudwatch")

# METRIC_NAMESPACE = os.environ.get("METRIC_NAMESPACE", "DedicatedHost/Observability")


# def lambda_handler(event, context):
#     print("Event received:")
#     print(json.dumps(event))

#     # Call EC2 DescribeHosts
#     response = ec2.describe_hosts()
#     hosts = response.get("Hosts", [])

#     total_hosts = len(hosts)
#     available = 0
#     maintenance = 0
#     assessment = 0

#     metric_data = []

#     for host in hosts:
#         host_id = host["HostId"]
#         state = host["State"]
#         capacity = host.get("AvailableCapacity", {})
#         instance_capacity = capacity.get("AvailableInstanceCapacity", [])

#         # Count states
#         if state == "available":
#             available += 1
#         elif state == "under-assessment":
#             assessment += 1
#         elif state == "maintenance":
#             maintenance += 1

#         # Calculate utilization per host
#         total_slots = 0
#         available_slots = 0

#         for item in instance_capacity:
#             total_slots += item.get("TotalCapacity", 0)
#             available_slots += item.get("AvailableCapacity", 0)

#         utilization = 0
#         if total_slots > 0:
#             utilization = ((total_slots - available_slots) / total_slots) * 100

#         metric_data.append({
#             "MetricName": "HostUtilizationPercent",
#             "Dimensions": [
#                 {"Name": "HostId", "Value": host_id}
#             ],
#             "Timestamp": datetime.datetime.utcnow(),
#             "Value": utilization,
#             "Unit": "Percent"
#         })

#     # Fleet-level metrics
#     metric_data.extend([
#         {
#             "MetricName": "TotalHosts",
#             "Timestamp": datetime.datetime.utcnow(),
#             "Value": total_hosts,
#             "Unit": "Count"
#         },
#         {
#             "MetricName": "AvailableHosts",
#             "Timestamp": datetime.datetime.utcnow(),
#             "Value": available,
#             "Unit": "Count"
#         },
#         {
#             "MetricName": "HostsInMaintenance",
#             "Timestamp": datetime.datetime.utcnow(),
#             "Value": maintenance,
#             "Unit": "Count"
#         },
#         {
#             "MetricName": "HostsUnderAssessment",
#             "Timestamp": datetime.datetime.utcnow(),
#             "Value": assessment,
#             "Unit": "Count"
#         }
#     ])

#     # Publish metrics (batching for safety)
#     for i in range(0, len(metric_data), 20):
#         cloudwatch.put_metric_data(
#             Namespace=METRIC_NAMESPACE,
#             MetricData=metric_data[i:i+20]
#         )

#     print("Metrics published successfully")

#     return {
#         "status": "success",
#         "total_hosts": total_hosts
#     }


#STEP 10: replace this handler.py to include the spreadscore and blastradius , zip again and apply







#variables
variable "region" {
  description = "AWS region"
  type        = string
}

variable "project" {
  description = "Aws migration of ec2 to dedicated Hosts"
  type        = string
  default     = "dedicated-host-observability"
}

variable "ccoe_account_id" {
  description = "CCOE AWS Account ID"
  type        = string
}
