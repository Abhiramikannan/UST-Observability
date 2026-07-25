```md
# Observe vs New Relic

## Observe

Observe is an observability tool, just like:

- Grafana
- New Relic
- Dynatrace

Its main job:

- Collect logs + metrics + traces
- Help you monitor systems & debug issues

---

# Q. How is it different from other Observability tools?

Difference is **HOW it stores data**.

- New Relic / Grafana → store data in database (indexed, structured)
- Observe → stores data in data lake (raw, flexible storage)

This is the biggest difference.

---

# Q. What is a data lake? (Very simple)

Think like this:

## Database (New Relic style)

- Structured
- Data must be clean & formatted before storing

Example:

**Table: metrics**

| Metric | Value |
|---------|------:|
| CPU | 70% |
| Memory | 80% |

## Data lake (Observe style)

A data lake = dump all data in raw format.

- Logs ✅
- Metrics ✅
- Traces ✅
- JSON ✅
- Any data ✅

No strict structure needed.

It stores everything first and organizes later.

---

# Q. How Observe stores data

## Step 1: Data comes from apps

- Logs from servers
- Metrics (CPU, latency)
- Traces (request flow)

## Step 2: Store in data lake

Stored in cheap storage like:

- S3 / cloud storage

Stored in formats like:

- Parquet
- Raw data

## Step 3: Query when needed

Instead of indexing everything:

- Data is stored raw
- Query engine reads and analyzes when needed

This is called:

> **Store first → Analyze later**

---

# Q. Why does the data lake matter?

In normal tools like New Relic:

- We filter logs.
- We sample traces.
- Storage is costlier.

In Observe:

- You can store full data.
- No need to drop data.
- Storage is cheap.

---

# Q. Advantages of moving from New Relic to Observe

- Cost advantage (data lake is cheaper)
- Can store ALL data (no data loss)
- No need to drop logs or sample traces
- Better data correlation (logs + metrics + traces can be stored together)

Easy to connect:

```

Error
↓
Trace
↓
Service
↓
Root Cause

```

- Unlimited users (no license cost)

---

# Q. Disadvantages of moving from New Relic to Observe

Observe has a few drawbacks compared to New Relic.

- It is newer.
- Fewer features and integrations.
- Mobile monitoring is weaker.
- Synthetic monitoring is weaker.
- More manual analysis using queries.
- Teams need to learn a new workflow compared to New Relic dashboards.

### Example

### New Relic

Problem:

```

CPU High

```

You:

- Open dashboard
- See CPU graph
- Done ✅

### Observe

Problem:

```

CPU High

```

You may need to:

- Search logs
- Query metrics
- Check traces
- Link everything

Example:

```

Show CPU usage for Service X
↓
Join with error logs
↓
Find related traces

```

In Observe, we may need to do some extra searching or querying to find the issue, whereas in New Relic we can directly see it in dashboards.

Also, when moving from New Relic, there will be some extra work to recreate dashboards, alerts, and setups, which can take time initially.

---

# Q. How much does ingestion of metrics and traces cost?

Observe charges based on data ingestion per GB.

- Metrics → around $0.01 per GB
- Traces → around $0.59 per GB

Overall cost depends on the total data volume sent.

---

# Q. How much does it cost for a customer to use Observe?

The cost mainly depends on how much data (logs, metrics, traces) the customer sends to the platform.

- No fixed license cost per user
- Customers pay based on data ingestion only
- Not based on number of users or licenses

---

# Q. If a customer plans to implement AI on Observe, how will it impact?

If the customer implements AI on Observe:

- Troubleshooting becomes faster.
- Manual effort is reduced.
- Data usage may increase.
- Cost may slightly increase.

Mostly around **10–30%** additional cost.

---

# Q. AI implementation: New Relic vs Observe

## New Relic

- Assistant-based AI
- We ask questions.
- AI analyzes and gives results.
- AI usage may consume compute units (extra cost)

## Observe

- Observe AI = Autonomous AI (AI SRE)
- Built-in AI
- No need to ask every time

When an alert comes:

AI automatically:

- Checks logs
- Checks metrics
- Checks traces
- Correlates everything

Provides:

- Root cause
- Suggested fix

---

# Q. MCP Server & ServiceNow Integration

## MCP Server

### New Relic

- Has MCP server

### Observe

- Already has its own MCP server
- Can connect to AI tools like:
  - Claude
  - Cursor
  - AI agents
- Still in an evolving stage

## ServiceNow Integration

Observe does **not** have a strong native ServiceNow integration like New Relic.

Possible using:

- APIs
- Custom integrations

Not plug-and-play.

---

# Q. Functionalities

## Same functionalities in New Relic and Observe

- Logs monitoring
- Metrics monitoring
- Distributed tracing
- Infrastructure monitoring (servers, cloud)
- Kubernetes / container monitoring
- Basic APM (Application Performance Monitoring)
- Dashboards
- Alerts
- Query / search capability
- AI support (different approach)

---

# Missing / Weaker in Observe (Compared to New Relic)

- Browser monitoring (RUM)
- Session replay
- Mobile app monitoring
- Synthetic monitoring (API / uptime testing)
- Large integration ecosystem (700+ tools)
- Direct ServiceNow integration
- Developer tools (CodeStream, IDE integration)
- Advanced code-level profiling
- Prebuilt dashboards and out-of-box features
- Mature UI/UX experience

---

# Missing in New Relic (Compared to Observe)

- AI SRE (automatic root cause analysis)
- Data lake architecture (store all data)
- Better cross-signal correlation (logs + metrics + traces)
- Lower cost at scale
- Unlimited users (no license limit)

---

# Observe Tool

## Overview

Observe is a cloud-native observability platform that helps engineers collect, store, analyze, and troubleshoot telemetry data from applications and infrastructure.

It unifies:

- Logs
- Metrics
- Traces
- Infrastructure monitoring

into a single platform to help teams quickly identify and resolve issues.

### Example

Imagine you have an application where the **checkout service is failing**.

With Observe, you can correlate:

- Logs
- Metrics
- Traces

together and find the root cause easily.

Observe stores all telemetry data in one place.

---

# Observe Architecture

## Telemetry Sources

Observe collects telemetry from different sources.

These sources generate:

- Logs
- Metrics
- Traces
- Events (MELT)

Observe collects telemetry using:

### OpenTelemetry Collector

Collects:

- Logs
- Metrics
- Traces

### Prometheus

Collects:

- Metrics

### APIs

External systems can push data into Observe.

Examples:

- Jenkins
- GitHub

### Shippers

Tools such as:

- Fluent Bit
- Fluentd
- Other log shippers

send logs to Observe.

---

## Secure Ingestion

Secure ingestion is done using:

- AWS VPC Endpoint (PrivateLink)

---

## Data Storage

After telemetry collection:

- Data is stored in a Data Lake.

---

## Data Processing

Observe enriches and correlates telemetry data and provides capabilities for:

- Monitoring
- Troubleshooting
- Root cause analysis
- Cross-signal correlation
```
