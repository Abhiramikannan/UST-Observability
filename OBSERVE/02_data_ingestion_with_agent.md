
# How Does Data Get into Observe?

There are two ways to ingest data into Observe:

1. **Using the Observe Agent**
2. **Without Using the Observe Agent**

---

# Task 1: Ingest Data Using the Observe Agent and Create a Dashboard

## Objective

In this task, you will:

1. Create an ingest token.
2. Create an Ubuntu virtual machine.
3. Install the Observe Agent.
4. Verify logs in Observe.
5. Verify CPU and Memory metrics.
6. Create your first dashboard.

---

# Step 1: Create an Ingest Token

Navigate to:

```text
Data & Integrations
    → Add Data
        → Integrations
            → Linux
                → Create Token
```

Copy the generated ingest token.

Example:

```text
ds152s5kvhBEOhdNDJlg:Yw_fAnYF_x7_jRgj9KQlpUyq__TMwdYU
```

> **Note:** This is an example token. Use the token generated for your environment.

---

# Step 2: Create an Ubuntu VM

Create an EC2 instance with the following configuration.

| Setting | Value |
|----------|-------|
| OS | Ubuntu Server 24.04 LTS |
| Instance Type | t3.micro (Recommended) |
| Key Pair | Create a new RSA key pair |
| Security Group | Create a new security group with **SSH** allowed from **My IP** (`launch-wizard-64`) |

Before connecting to the VM, ensure that:

- Instance status checks have passed.

---

# Step 3: Install the Observe Agent

After creating the VM:

1. Log in to Observe.
2. Navigate to:

```text
Data & Integrations
    → Add Data
        → Integrations
            → Linux
                → Create Token
```

3. Copy the ingest token.
4. Copy the installation commands displayed under **Integration Configuration**.
5. Run those commands on the Ubuntu VM.

### Observe UI

<img width="879" height="411" alt="image" src="https://github.com/user-attachments/assets/e79c111d-07bd-4ed4-b5cf-45156a0102a1" />

---

## Verify the Agent Status

Run:

```bash
observe-agent status
```

Example output:

```text
ubuntu@ip-172-31-27-195:~$ observe-agent status

================
Agent
================

Host Info
================

HostID: ec228c1d-a7b2-b906-111d-c6f61e026d4c
Hostname: ip-172-31-27-195
BootTime: 2026-06-26T07:43:59Z
Uptime: 14m47s
OS: linux
Platform: ubuntu
PlatformFamily: debian
PlatformVersion: 24.04
KernelArch: x86_64
KernelVersion: 6.17.0-1017-aws

Agent Metrics
================

ExporterQueueSize: 0
CPUSeconds: 0.48s
MemoryUsed: 138.10938MB
TotalSysMemory: 54.334236MB
Uptime: 8.282313s
AvgServerResponseTime: 0ms
AvgClientResponseTime: 0ms

Logs Stats
================

ReceiverAcceptedCount: 45
ReceiverRefusedCount: 0
ExporterSentCount: 45
ExporterSendFailedCount: 0

Metrics Stats
================

ReceiverAcceptedCount: 325
ReceiverRefusedCount: 0
ExporterSentCount: 210
ExporterSendFailedCount: 0

Traces Stats
================

ReceiverAcceptedCount: 0
ReceiverRefusedCount: 0
ExporterSentCount: 0
ExporterSendFailedCount: 0

Agent Health
================

Status: Running
TotalRefusedCount: 0
TotalSendFailedCount: 0
```

The above output confirms that:

- The Observe Agent is running correctly.
- Logs are being sent to Observe.
- Metrics are being sent to Observe.

---

# Step 4: Verify Logs in Observe

Log in to the Observe UI.

Navigate to the same Linux integration page where the installation commands were copied.

Click **Check Status**.

Wait approximately **2 minutes**.

### Check Status

<img width="940" height="192" alt="image" src="https://github.com/user-attachments/assets/3cb89e62-276f-44fa-8319-e2b1f2ee820b" />

---

After the status check completes, you should see:

<img width="940" height="309" alt="image" src="https://github.com/user-attachments/assets/4f703faf-a33a-4629-adf0-fbbe5c7a0fe4" />

---

Navigate to:

```text
Logs
```

Select:

```text
Host Logs
```

from the dropdown.

<img width="896" height="475" alt="image" src="https://github.com/user-attachments/assets/35d337e2-8f9a-49bd-a7b0-fe6214ef340b" />

<img width="940" height="443" alt="image" src="https://github.com/user-attachments/assets/114cc6ac-8268-4397-beb1-5a56998bbe47" />

---

## Generate a Test Log

From the VM terminal, run:

```bash
logger "Hello from Abhirami's Observe Lab"
```

Wait approximately **3 minutes**.

You should see the log in Observe.

> **Note:** During this lab, the log was not visible.

---

# Step 5: Verify Metrics in Observe

Navigate to:

```text
Metrics
```

Select:

```text
Prometheus Metrics
```

from the sidebar.

<img width="940" height="432" alt="image" src="https://github.com/user-attachments/assets/ea3af4de-3d57-4929-8897-607dc55c9168" />

Verify that CPU and Memory metrics are being collected from the Ubuntu VM.

---

# Step 6: Create Your First Dashboard

After verifying that:

- Logs are successfully ingested.
- Metrics are successfully collected.

Create your first Observe dashboard using the collected telemetry data.

Dashboard:
<img width="940" height="378" alt="image" src="https://github.com/user-attachments/assets/78a22a67-72ca-4caa-99f2-bce90bf6f134" />

