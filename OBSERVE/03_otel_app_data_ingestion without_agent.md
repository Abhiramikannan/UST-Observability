
# Task 2: Configure OpenTelemetry (OTel) Datastream in Observe

This task demonstrates how to configure an **OTel Datastream** in Observe and send OpenTelemetry telemetry (Logs, Metrics, and Traces) from an OpenTelemetry Collector.

---

# Step 1: Create an OTel Datastream

Navigate to:

```text
Data & Integrations
    → Datastreams
        → OTel Connector
```

Create a new datastream.

---

# Step 2: Datastream Generates an Endpoint and Token

When the datastream is created, Observe automatically generates:

## 1. Observe OTLP Ingestion Endpoint

```text
https://<CUSTOMER-ID>.collect.observeinc.com/v2/otel
```

## 2. Authentication Token

```text
Bearer <OBSERVE_DATASTREAM_TOKEN>
```

> **Note**
>
> Replace the endpoint URL and token with the values generated for your Observe tenant.
>
> Do **not** hardcode production tokens in configuration files or documentation.

Example:

| Property | Value |
|----------|-------|
| Token Name | otel token |
| Datastream | OTEL Connector |

---

# Why Are the Endpoint URL and Token Required?

The OpenTelemetry Collector requires two pieces of information to send telemetry to Observe:

1. **Observe OTLP Ingestion Endpoint**
2. **Datastream Authentication Token**

The collector sends telemetry to the Observe endpoint and authenticates every request using the datastream token.

Without these two values, the OpenTelemetry Collector cannot send data to Observe.

---

# What is the Observe OTLP Ingestion Endpoint?

Example:

```text
https://<tenant-id>.collect.observeinc.com/v2/otel
```

This URL is the **Observe OTLP Ingestion Endpoint**.

It acts as the **entry point (front door)** for receiving OpenTelemetry telemetry into Observe.

The OpenTelemetry Collector sends data to this endpoint over HTTPS.

The endpoint receives:

- Logs
- Metrics
- Traces

and stores them inside Observe.

Without this endpoint URL, the OpenTelemetry Collector would not know where to send the application's telemetry data.

---

# Step 3: Configure the OpenTelemetry Collector

Update the **config.yaml** file.

> **Important**
>
> The `Authorization` header uses the **Datastream Authentication Token** that was generated when the OTel Datastream was created.

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

  otlphttp/observe:
    endpoint: https://<OBSERVE_CUSTOMER_ID>.collect.observeinc.com/v2/otel

    headers:
      Authorization: "Bearer <OBSERVE_DATASTREAM_TOKEN>"

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
        - debug

    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - prometheus
        - otlphttp/observe
        - debug

    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - loki
        - otlphttp/observe
        - debug
```
---

- Give this config file to shifa or Rahul they will apply the changes then only the data will be sent.
otlphttp/observe   : this observe is just a label.
---

# Step 4: Verify Data Ingestion

Navigate to:

```text
Data & Integrations
    → Datastreams
        → OTEL Connector
            → otel token
                → Data
```

The **Data** tab displays the telemetry that has been received through the datastream.

<img width="912" height="429" alt="image" src="https://github.com/user-attachments/assets/0837f448-5cbd-47b6-b8ee-11d658aa5af5" />

---

# Current Observation

Although telemetry was being sent to the datastream, no data was visible in:

- Logs
- Metrics
- Traces

To make the data easier to query and visualize, create datasets.

---

# Step 5: Create Datasets

Navigate to:

```text
Datasets
    → OTEL Connector
        → Open in Worksheet
```

Create two datasets:

- OTel Metrics
- OTel Logs

After creating each dataset, **Publish** it.

---

# Switch to the OPAL Query Editor

Open the worksheet and switch to the **OPAL Query Editor**.

<img width="940" height="176" alt="image" src="https://github.com/user-attachments/assets/63b56c44-62ae-42ad-a6bc-3aa0fc1aa6a9" />

---

# Create the OTel Metrics Dataset

Run the following OPAL query to filter only OpenTelemetry metrics.

```opal
filter OBSERVATION_KIND = "otelmetrics"
make_col metric:string(FIELDS.name)
make_col value:float64(FIELDS.value)
make_col timestamp:BUNDLE_TIMESTAMP
make_col service_name:string(EXTRA.resource.attributes."service.name")
make_col host_name:string(EXTRA.resource.attributes."host.name")
set_valid_from options(max_time_diff:4h), timestamp
interface "metric", metric: metric, value:value
```

After verifying the output:

1. Create a new dataset.
2. Publish the dataset.

---

# Create the OTel Logs Dataset

Run the following OPAL query to filter only OpenTelemetry logs.

```opal
filter OBSERVATION_KIND = "otellogs"
make_col timestamp:BUNDLE_TIMESTAMP
make_col body:string(FIELDS.logs.body)
make_col severity:string(FIELDS.logs.severity_text)
make_col service_name:string(FIELDS.resource.attributes."service.name")
make_col host_name:string(FIELDS.resource.attributes."host.name")
set_valid_from options(max_time_diff:4h), timestamp
interface "log", log:body
```

After verifying the output:

1. Create a new dataset.
2. Publish the dataset.

---

# OTel Logs Dataset

Reference:

```text
https://113700876252.observeinc.com/workspace/43162862/dataset/Otel-logs-43171574?v-tab=definition&s=62933-u743bns9
```

---

# Result

After publishing the datasets:

- OTel Logs dataset is available.
- OTel Metrics dataset is available.
- These datasets can now be used in dashboards, worksheets, alerts, and further analysis.

## How to add a markdown variable in Observe:
<img width="940" height="540" alt="image" src="https://github.com/user-attachments/assets/d1cf6420-5310-4d5b-af1e-b3eaebc0378a" />
<img width="940" height="324" alt="image" src="https://github.com/user-attachments/assets/5f85c6a9-cd93-4ac3-9641-4461904496be" />

