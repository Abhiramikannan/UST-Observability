28/07/2025

Observability:
Observability is the ability to understand what is happening inside a system just by looking at its external outputs (like logs, metrics, and traces). 
It helps teams detect, diagnose, and resolve issues in complex software systems.

BIG PUZZLE:
<img width="1354" height="845" alt="image" src="https://github.com/user-attachments/assets/5cab3c59-9b08-4236-8563-12756fc375b2" />

 1. Known-Knowns :
    We know the problem AND the solution.
    have 10 no of users,move to 100 no of users->scale(could be on cloud,on-premise ->depends on saying that u defined the threshholds)
    eg: You know CPU usage goes high when user traffic increases.
        You already know to scale the app up in such cases.
        Tools/Actions:Dashboards,Dynamic thresholding,Alerts,Automation
        Goal: Make what you know work even better (optimize).
 2. Known-Unknowns:
    We know something is wrong, but we don’t know why.
    eg: Latency spike is visible in the dashboard, but you don’t know the root cause.
         Latency is the time between a user making a request and the system responding to it.
         A latency spike means the response time suddenly increased — maybe for a few seconds, or minutes.
         Your normal response time = 200ms
         But suddenly, it becomes = 1.5 seconds
         tools/actions: Auto-correlation,Real-time analytics,Business process mining
    Goal: Use smart tools to dig into the data and figure out the reason.
 3. Unknown-Knowns:
    We have the data but didn’t realize something’s wrong until analysis.
         eg: You already collect disk usage metrics, but never noticed it's been slowly increasing.Once you do anomaly detection, you discover this issue.
         Tools/Actions: Anomaly detection,Predictive alerts,Log analysis
    Goal: Turn hidden problems into known ones before they cause failure.
    anolomy detection: where u look upon ur existing system.Because u defined ur monitoring,threshhold->see whats deviating: maybe ur cpu,memory,etc.

4. Unknown-Unknowns:
   We don’t know there’s a problem, and we don’t know what to look for.
   eg:
        Suddenly your system fails for no apparent reason,
        There were no symptoms. Everything looked fine,
        Like a sudden heart attack with no warning.
    Tools/Actions: Deep observability, AI/ML to detect patterns, Flexible monitoring (ingest all data, open-ended queries)
    Goal: Prepare for the unexpected. Build a system that can tell you: "Hey, something strange is happening, even if you didn’t know to check for it!"

key points:
We want to become predictable — to avoid surprises.We can’t know everything in advance — especially unknown unknowns.That’s where observability becomes powerful:It helps us see what we didn’t even think to monitor.

    

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

SYMPTOMS VS CAUSES:
<img width="1423" height="852" alt="image" src="https://github.com/user-attachments/assets/ab37c224-7aa8-4dc5-bc25-c1d4d1a0200a" />
 1. Symptoms (Top of the Temple):
      “Something is broken” – you can see the impact, but not yet know why.
       Examples:High latency, Errors in dashboard, App not loading, Service down
    This is what traditional monitoring shows — the “what”.
    Monitoring: when it reaches above threshold(cpu,memory) -we take actions(alerts).

    
 2. The Pillars (Middle) — Logs, Metrics, Traces, etc.
      These are your data signals — used to investigate and debug. They help answer the question:"Why is this broken?"
    
| Pillar       | What it helps you do                                           |
| ------------ | -------------------------------------------------------------- |
| **Logs**     | Detailed events and errors (e.g. error 500 in payment service) |
| **Events**   | Changes like deployments, restarts                             |
| **Metrics**  | Numbers over time (CPU, memory, latency, request count)        |
| **Profiles** | System behavior (CPU time per function, memory leaks)          |
| **Traces**   | End-to-end request flow (microservices call chain)             |

These are used during debugging, profiling, and tracing — part of observability (not just monitoring).

3. Causes (Bottom)
   The root cause of the issue. What exactly failed and why?
    Examples: A slow DB query, A memory leak in version 1.2.5, One microservice timed out, A deployment broke a config
This part requires active investigation using observability signals (those pillars).

Reactive vs Proactive:
 Traditional monitoring is reactive → "Alert fired, now go check"
 Observability enables proactive debugging → "Let's find the root cause using data"

  DevOps Example to Make It Real:
   You get an alert: “API latency > 3s”
   Monitoring tells you: There’s a spike
   Observability tells you:
   Logs: A timeout occurred in payment service, 
   Metrics: CPU on one pod is 100%,
   Traces: Slow DB query took 2.8s,
   Cause: DB index missing → fix.
  Without observability, you’re guessing. With observability, you’re investigating with data.
   observability is essential when systems get complex and distributed.

 What is Instrumentation?
  Instrumentation means adding monitoring code in the application so you can track internal behavior, especially when errors are not easily visible.
  In Java, developers often use:
    System.out.println("Step X reached. Variable value: " + myVar);
   This log gets printed when a specific block is executed.
  This helps understand what the system was doing before it failed.
  Developers add such lines intentionally, even if no error occurs, just to trace and measure.

  What is Wisdom of Production?
    If something breaks in production, use that experience to improve the code.
    The DevOps or Observability team sees the issue in production (like a latency spike), informs the development team, and they update the code by instrumenting it better.
So, next time, instead of guessing, logs and metrics will reveal what went wrong.

What is OpenTelemetry?
  OpenTelemetry is a tool that helps you watch what your app is doing.
  It helps collect:

Traces – what happened and when

Metrics – how much or how long something took

Logs – messages about what your app is doing

eg: If a website is slow, OpenTelemetry helps you:
  Track where the request went,
  See which service or database is slow,
  Understand the full path of the request.


1. OpenTelemetry Enables Auto-Instrumentation
     Manual instrumentation = Developers write extra code to track metrics, logs, traces.

     Auto instrumentation means OpenTelemetry can automatically track things like website requests and database calls without you writing extra code.

   This is critical because:

           Modern apps = 1000s of microservices, libraries, layers.
           
           You can’t manually trace everything — too slow and error-prone.
           
            OpenTelemetry makes observability scalable and developer-friendly.

 2.  Observability → Visibility Into Unknown Issues

Traditional monitoring finds known issues (e.g., CPU > 90%).

Observability helps you detect unknown problems — like:

       A new bug after deployment
       
       A service timing out randomly
       
       A hidden slow API dependency

3. Incident Resolution Becomes Faster and Smarter
   Observability makes it easier to:
     Detect an issue early (fast alerts)
     Debug it quickly using traces, logs, metrics
     Fix it faster → Reduce downtime
   
4. Reducing Operational Cost (Toil Reduction)
   Toil reduction means removing or reducing boring, repetitive, manual tasks that don't add much value — especially when they can be automated.
   Support work costs money. To save money:

         Use chatbots to fix common issues (25% incidents solved = big savings).
         
         Automate boring, repeated tasks (like restarting a service).
         
         In SRE, this boring work is called toil — it’s manual, repetitive, and can be automated. So, we try to remove it.

5.  Measure Team Velocity and Business Value:
It’s not just about releasing features — it’s about delivering real value.

So, we observe things like:
     
     How much work the team completes (e.g., story points)
     
     How often we release (deployment frequency)
     
     How fast users benefit from our changes

6. SLA → SLO → SLI
   "Move from Service Level Agreements to Service Level Objectives."
| Term    | What it Means                                                                    |
| ------- | -------------------------------------------------------------------------------- |
| **SLA** | External, legal: "We promise 99.9% uptime"                                       |
| **SLO** | Internal, engineering goal: "Let’s keep latency under 300ms for 95% of requests" |
| **SLI** | Actual measurement: “Latency p95 = 278ms”                                        |

SLOs help you measure and improve user experience realistically, not just legally.

   
   
  
      


