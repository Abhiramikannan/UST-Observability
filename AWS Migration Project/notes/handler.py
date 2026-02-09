import boto3
import os
import json
import datetime
from collections import defaultdict

ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")

METRIC_NAMESPACE = os.environ.get(
    "METRIC_NAMESPACE", "DedicatedHost/Observability"
)


def lambda_handler(event, context):
    print("Event received:")
    print(json.dumps(event))

    timestamp = datetime.datetime.utcnow()

    # -----------------------------
    # 1. Describe Dedicated Hosts
    # -----------------------------
    hosts_resp = ec2.describe_hosts()
    hosts = hosts_resp.get("Hosts", [])

    total_hosts = len(hosts)
    host_ids = {h["HostId"] for h in hosts}

    print(f"Total Dedicated Hosts: {total_hosts}")

    # -----------------------------
    # 2. Describe Instances (CCOE only)
    # -----------------------------
    instances_resp = ec2.describe_instances()
    reservations = instances_resp.get("Reservations", [])

    instances_per_host = defaultdict(int)
    total_instances = 0

    for r in reservations:
        for inst in r.get("Instances", []):
            placement = inst.get("Placement", {})
            host_id = placement.get("HostId")

            # Only count instances placed on Dedicated Hosts
            if host_id:
                instances_per_host[host_id] += 1
                total_instances += 1

    hosts_used = len(instances_per_host)
    max_instances_on_single_host = (
        max(instances_per_host.values())
        if instances_per_host else 0
    )

    print(f"Total Instances (visible): {total_instances}")
    print(f"Hosts Used: {hosts_used}")

    # -----------------------------
    # 3. Calculate Risk Metrics
    # -----------------------------
    spread_score = 0.0
    blast_radius = 0.0

    if total_instances > 0 and total_hosts > 0:
        spread_score = (
            hosts_used / min(total_hosts, total_instances)
        ) * 100

        blast_radius = (
            max_instances_on_single_host / total_instances
        ) * 100

    print(f"SpreadScore: {spread_score}")
    print(f"BlastRadius: {blast_radius}")

    # -----------------------------
    # 4. Prepare CloudWatch Metrics
    # -----------------------------
    metric_data = [
        {
            "MetricName": "TotalHosts",
            "Timestamp": timestamp,
            "Value": total_hosts,
            "Unit": "Count"
        },
        {
            "MetricName": "TotalInstances",
            "Timestamp": timestamp,
            "Value": total_instances,
            "Unit": "Count"
        },
        {
            "MetricName": "SpreadScore",
            "Timestamp": timestamp,
            "Value": spread_score,
            "Unit": "Percent"
        },
        {
            "MetricName": "BlastRadius",
            "Timestamp": timestamp,
            "Value": blast_radius,
            "Unit": "Percent"
        }
    ]

    # Per-host instance count
    for host_id, count in instances_per_host.items():
        metric_data.append({
            "MetricName": "InstancesPerHost",
            "Dimensions": [
                {"Name": "HostId", "Value": host_id}
            ],
            "Timestamp": timestamp,
            "Value": count,
            "Unit": "Count"
        })

    # -----------------------------
    # 5. Publish Metrics (batch of 20)
    # -----------------------------
    for i in range(0, len(metric_data), 20):
        cloudwatch.put_metric_data(
            Namespace=METRIC_NAMESPACE,
            MetricData=metric_data[i:i + 20]
        )

    print("Risk metrics published successfully")

    return {
        "status": "success",
        "total_hosts": total_hosts,
        "total_instances": total_instances,
        "spread_score": spread_score,
        "blast_radius": blast_radius
    }


#zip lambda.zip handler.py
#terraform apply
