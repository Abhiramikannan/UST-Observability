28/07/2025

Observability:
Observability is the ability to understand what is happening inside a system just by looking at its external outputs (like logs, metrics, and traces). 
It helps teams detect, diagnose, and resolve issues in complex software systems.

BIG PUZZLE:
<img width="1354" height="845" alt="image" src="https://github.com/user-attachments/assets/5cab3c59-9b08-4236-8563-12756fc375b2" />



CORE ANALYSIS LOOP:
<img width="1391" height="707" alt="image" src="https://github.com/user-attachments/assets/7c4258f1-87ec-45fb-927f-07254435a38d" />

telemetry data: logs,metrices,traces

steps:
1. What are you trying to understand?
     Example: “Why did our application latency spike yesterday?” or “Why is there a sudden drop in CPU usage?”
2. Visualize telemetry data to find relevant performance anomalies
    Look at metrics, logs, traces, dashboards, etc., to spot irregularities.
    Tools: Azure Monitor, Grafana, Prometheus, etc.
    Goal: Identify where and when the problem starts.
3. Search for common dimensions within the anomalous area
     Group by service name?
     Filter by region?
     version (v1.2.3 vs v1.2.4)
     user type
     instance(pod1,pod2)
     Compare time ranges?
   This helps narrow down the issue to patterns or causes.
   You group or filter by these dimensions to find a pattern.
   “Is this issue happening only for certain pods? Or only after a new deployment? Or only in one region?”

5. Evaluate
     “Did my filtering/grouping help me find something meaningful?”
   if yes-> got a clue ->“Only version v1.2.4 of the app is failing in us-east region.”->Go back to step 1 with a narrower question:What changed in version v1.2.4?->You now dig deeper into the real root cause.

   if no->You didn’t find anything useful yet.->So, go back to Step 2 or 3, and try filtering using different attributes.->This time filter by customer type,check API endpoint paths.

Why This Is a Loop?
  Visualize → Filter → Think → Repeat

| Step           | What you do                                                 | Example                                            |
| -------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| 1. Define Goal | Ask what you want to understand                             | Why is login slow?                                 |
| 2. Visualize   | Check dashboards/logs/metrics                               | Latency spike at 3 PM                              |
| 3. Analyze     | Filter/group by attributes                                  | Only `v1.2.4` in `us-east` is affected             |
| 4. Evaluate    | Did this help? If yes, go deeper. If not, try another view. | Found faulty pod, or repeat with different filters |


