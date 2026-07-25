# Logz.io Integration Guide

## 1. Connecting an OpenTelemetry Application with Logz.io

### Prerequisites

* Ensure your application is using the **OpenTelemetry Collector Contrib** image.
* Verify that your `docker-compose.yaml` is using the **contrib collector**.

Example:

```yaml
image: otel/opentelemetry-collector-contrib:0.111.0
```

If you encounter the following error:

```
unknown exporter type "logzio"
```

update the collector image to one of the following:

```yaml
image: otel/opentelemetry-collector-contrib:0.111.0
```

or

```yaml
image: otel/opentelemetry-collector-contrib:latest
```

> **Note:** The Logz.io documentation referenced was generated for Collector **0.111.0**. Older versions (such as **0.96.0**) may not support all Logz.io exporters.

---

## Logz.io OpenTelemetry Tokens

Logz.io does **not** recommend using the generic `otlphttp` exporter. Instead, it provides dedicated OpenTelemetry exporters that use separate shipping tokens for each telemetry type.

Navigate to:

```
Integrations → OpenTelemetry
```

Copy the following shipping tokens:

| Telemetry Type | Shipping Token                     |
| -------------- | ---------------------------------- |
| Logs           | `gxsYFKoqybeSlgkgMBiUviAHwkieSQZU` |
| Metrics        | `ssGtUiPkQcVIXxMKMueFfPoUEffoOctB` |
| Traces         | `jSDYvjnytFhUmLVdmaureBNBpUrIIKqk` |

Update the OpenTelemetry Collector configuration with these tokens.

---

## Why Not Use the Generic OTLP HTTP Exporter?

Different observability platforms have different recommendations.

* **Observe** and **New Relic** expose standard **OTLP endpoints**, so the `otlphttp` exporter is the recommended approach.
* **Logz.io** provides and recommends **dedicated Logz.io exporters** in its official OpenTelemetry documentation. These exporters handle authentication and ingestion specifically for Logz.io.

Therefore:

* **Observe → OTLP HTTP Exporter**
* **New Relic → OTLP HTTP Exporter**
* **Logz.io → Dedicated Logz.io Exporters**

---

## config file

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
    endpoint: https://<customer-id>.collect.observeinc.com/v2/otel
    headers:
      Authorization: "<datastream-token>"
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

  otlphttp/observe_terraform:
    endpoint: https://<customer-id>.collect.observeinc.com/v2/otel
    headers:
      Authorization: "<datastream-token>"
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

  otlphttp/newrelic:
    endpoint: https://otlp.nr-data.net
    headers:
      api-key: <apikey>
 
  logzio/logs:
    account_token: gxsYFKoqybeSlgkgMBiUviAHwkieSQZU
    region: us
    headers:
      user-agent: logzio-opentelemetry-logs

  prometheusremotewrite/logzio:
    endpoint: https://listener.logz.io:8053
    headers:
      Authorization: "Bearer ssGtUiPkQcVIXxMKMueFfPoUEffoOctB" 
      user-agent: logzio-opentelemetry-metrics
    target_info:
      enabled: false

  logzio/traces:
    account_token: jSDYvjnytFhUmLVdmaureBNBpUrIIKqk
    region: us
    headers:
      user-agent: logzio-opentelemetry-traces
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
        - otlphttp/newrelic
        - logzio/traces
        - debug
 
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - prometheus
        - otlphttp/observe
        - otlphttp/observe_terraform
        - otlphttp/newrelic
        - prometheusremotewrite/logzio
        - debug
 
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters:
        - loki
        - otlphttp/observe
        - otlphttp/observe_terraform
        - otlphttp/newrelic
        - logzio/logs
        - debug
```
---

## Verification

After updating the collector configuration:

1. Restart the OpenTelemetry Collector.
2. Generate sample logs, metrics, and traces.
3. Verify that the telemetry appears in the Logz.io portal.

**Status:** Configuration was updated successfully by **Shifa**, and the telemetry ingestion was verified.

---

# 2. Connecting to Logz.io Using Python APIs

## Step 1: Generate an API Token

Navigate to:

```
Settings → Manage Tokens
```

Copy the **API Token**.

Example:

```text
API_TOKEN = "e57af99a-8e59-4eee-abe2-8661cfc05ea0"
```

> **Note:** This API token is different from the shipping tokens used by the OpenTelemetry Collector.

---

## Step 2: Logz.io API Details

### Base URL

```text
https://api.logz.io
```

### Search Endpoint

```text
https://api.logz.io/v1/search
```

---

## Step 3: Authentication Headers

Use the API token in the request header.

```python
headers = {
    "X-API-TOKEN": API_TOKEN,
    "Content-Type": "application/json"
}
```

---

## Step 4: API Configuration Summary

| Parameter             | Value                                       |
| --------------------- | ------------------------------------------- |
| Base URL              | `https://api.logz.io`                       |
| Search Endpoint       | `https://api.logz.io/v1/search`             |
| Authentication Header | `X-API-TOKEN`                               |
| Content Type          | `application/json`                          |
| Authentication Token  | API Token from **Settings → Manage Tokens** |

---
# how we can connect and run query of newrelic in python code using API connection.

	Generate New Relic API Key (New Relic →profile icon ->  Administration → API Keys)
	Key name : otel-newrelic
	Key: <apikey>
	Get account Id: 
7291193
	GRAPHQL_URL = https://api.newrelic.com/graphql


