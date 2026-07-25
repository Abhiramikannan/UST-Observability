# Update the OpenTelemetry Collector Configuration

To recreate the dashboard successfully in the new Observe account, the **OTel Demo Application** must also send its telemetry (Logs, Metrics, and Traces) to the new Observe account.

Update the OpenTelemetry Collector configuration (`config.yaml`) by adding an additional Observe exporter for the new account.

> **Note**
>
> The new exporter uses:
>
> - The **Observe Customer ID** of the new account.
> - The **Datastream Authentication Token** generated from the new account.
>
> This allows the OTel Demo Application to send telemetry to both the original Observe account and the new Observe account simultaneously.

Example:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 1024

  memory_limiter:
    check_interval: 5s
    limit_mib: 256

exporters:
  prometheus:
    endpoint: 0.0.0.0:8889
    namespace: otel
    resource_to_telemetry_conversion:
      enabled: true

  otlp/tempo:
    endpoint: tempo:4317
    tls:
      insecure: true

  loki:
    endpoint: http://loki:3100/loki/api/v1/push
    default_labels_enabled:
      exporter: true
      job: true

  # Existing Observe Account
  otlphttp/observe:
    endpoint: https://<SOURCE_CUSTOMER_ID>.collect.observeinc.com/v2/otel
    headers:
      Authorization: "Bearer <SOURCE_DATASTREAM_TOKEN>"

    compression: gzip

    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s

    sending_queue:
      enabled: true
      num_consumers: 4
      queue_size: 1000

  # New Observe Account (Terraform Restore)
  otlphttp/observe_terraform:
    endpoint: https://<TARGET_CUSTOMER_ID>.collect.observeinc.com/v2/otel

    headers:
      Authorization: "Bearer <TARGET_DATASTREAM_TOKEN>"

    compression: gzip

    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s

    sending_queue:
      enabled: true
      num_consumers: 4
      queue_size: 1000

  debug:
    verbosity: basic

service:
  pipelines:

    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - otlp/tempo
        - otlphttp/observe
        - otlphttp/observe_terraform
        - debug

    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - prometheus
        - otlphttp/observe
        - otlphttp/observe_terraform
        - debug

    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - loki
        - otlphttp/observe
        - otlphttp/observe_terraform
        - debug
```

## Why are two Observe exporters configured?

Two Observe exporters are configured so that the OpenTelemetry Collector sends the same telemetry to both Observe environments.

- **`otlphttp/observe`**
  - Sends telemetry to the original Observe account.

- **`otlphttp/observe_terraform`**
  - Sends telemetry to the new Observe account where the dashboard is being recreated.

This ensures that:

- Both Observe accounts receive identical Logs, Metrics, and Traces.
- The recreated datasets receive live telemetry.
- The recreated dashboard displays data immediately after it is deployed using Terraform.

# Recreating Observe Dashboards Using Terraform

Observe dashboards can be exported as Terraform code and recreated using Terraform.

There are two export options:

## 1. Terraform (Recommended)

Use this option when recreating a dashboard in the **same Observe account**.

- Export the dashboard as **Terraform (Recommended)**.
- Save the generated `.tf` file locally. eg: dashboard.tf
- Use Terraform to recreate the dashboard in the same Observe account.

---

## 2. Cross-Customer Terraform

Use this option when recreating a dashboard in a **different Observe account**.

- Export the dashboard as **Cross-Customer Terraform**.
- Save the generated `.tf` file locally. eg: dashboard.tf
- Use Terraform to recreate the dashboard in another Observe account.

> **Note**
>
> Observe does **not** provide an import option for dashboards.
> Dashboard recreation is performed entirely using Terraform.

---

# Migrating a Dashboard to Another Observe Account

Before recreating the dashboard in another Observe account, back up the following:

- Dashboard (Cross-Customer Terraform)
- Required Datasets

Since dashboards depend on datasets, the datasets must be recreated first.

---

# Step 1: Export the Dashboard

Open the dashboard.

Select:

```text
Export
    → Cross-Customer Terraform
```

Save the generated `.tf` file locally.

Example:

```text
dashboard.tf
```

---

# Step 2: Export the Required Datasets

Create Terraform definitions for the datasets required by the dashboard. Export 2 datasets and create as a single datasets.tf file 

Example:

```text
datasets.tf
```

This file should contain the Terraform resources for:

- OTel Logs Dataset
- OTel Metrics Dataset

---

# Recreating in the New Observe Account

## New Observe Account

| Property | Value |
|----------|-------|
| Customer ID | 121661270020 |
| Workspace ID | 43175988 |
| Working Directory | /home/ec2-user/observe-restore |

Workspace URL

```text
https://121661270020.observeinc.com/workspace/43175988/home
```

---

# Step 3: Create a Service Account Token

Generate a **Service Account Token** in the new Observe account.

This token is used by Terraform to authenticate with Observe.

It will be configured in:

```text
providers.tf
```

---

# Step 4: Prepare the Terraform Environment

Create a working directory.

Example:

```text
/home/ec2-user/observe-restore
```

Install Terraform.

Create:

```text
providers.tf
```

Configure it with:

- Customer ID
- Workspace ID
- Service Account Token

The provider configuration should point to the **new Observe account**.

---

# Step 5: Create the Datastream

Navigate to:

```text
Data & Integrations
    → Datastreams
```

Create a new datastream.

Example:

```text
otel-datastream
```

---

# Step 6: Create a Datastream Token

Create a token for the datastream.

Example:

```text
otel-token
```

Observe generates a Datastream Authentication Token.

This token will be used in the application's **config.yaml**.

Update the OpenTelemetry exporter with:

- New Observe Customer ID
- New Datastream Token

Example:

```yaml
exporters:
  otlphttp/observe:
    endpoint: https://<OBSERVE_CUSTOMER_ID>.collect.observeinc.com/v2/otel

    headers:
      Authorization: "Bearer <OBSERVE_DATASTREAM_TOKEN>"
```

The OpenTelemetry Collector will use this endpoint and token to send telemetry to the new Observe account.

---

# Step 7: Verify the Datastream

A sample request can be sent to verify that the datastream is reachable.

Example:

```bash
curl https://<OBSERVE_CUSTOMER_ID>.collect.observeinc.com/v1/http \
  -H "Authorization: Bearer <OBSERVE_DATASTREAM_TOKEN>" \
  -H "Content-type: application/json" \
  -d '{"data":"hello world"}'
```

---

# Step 8: Initialize Terraform

Run:

```bash
terraform init
```

Terraform should initialize successfully.

---

# Step 9: Get the Dataset ID

Navigate to:

```text
Datasets
    → otel-datastream
```

Open the automatically created dataset.

Copy the dataset URL.

Example:

```text
https://121661270020.observeinc.com/workspace/43175988/dataset/otel-datastream-43180028
```

From the URL:

- Customer ID
- Workspace ID
- Dataset ID

can be identified.

Example:

```text
Dataset ID = 43180028
```

---

# Step 10: Create datasets.tf

Create a Terraform file containing the required datasets.

Example:

```text
datasets.tf
```

Include:

- OTel Logs Dataset
- OTel Metrics Dataset

---

# Step 11: Review the Dataset Changes

Run:

```bash
terraform plan
```

---

# Step 12: Create the Datasets

Apply only the dataset resources.

```bash
terraform apply \
  -target=observe_dataset.otel_metrics \
  -target=observe_dataset.otel_logs
```

This recreates the datasets in the new Observe account.

---

# Step 13: Restore the Dashboard

Copy the exported **Cross-Customer Terraform** dashboard file into the Terraform working directory.

Example:

```text
dashboard.tf
```

---

# Step 14: Review the Dashboard Changes

Run:

```bash
terraform plan
```

---

# Step 15: Create the Dashboard

Run:

```bash
terraform apply
```

Terraform recreates the dashboard in the new Observe account.

---

# Result

After Terraform completes successfully:

- The datastream is configured.
- The OpenTelemetry Collector sends telemetry to the new Observe account.
- The required datasets are recreated.
- The dashboard is recreated using Terraform.
- The dashboard is fully functional in the new Observe account.
