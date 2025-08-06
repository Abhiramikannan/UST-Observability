06/08/25

SRE REQUIREMENTS OF METRICS DATA

Q. what is Prometheus?
           Collects and stores metrics
          Prometheus is an open-source monitoring and alerting toolkit designed to collect and query metrics from systems and applications.
          
Q. What Prometheus Does:
                Collects metrics from applications and systems at regular intervals
                
                Stores the data in a time-series database
                
                Allows powerful queries using its own query language called PromQL
                
                Supports visualizations through tools like Grafana
                
                Triggers alerts when something goes wrong (through Alertmanager)

      Example Use Case:You're running a web application. Prometheus can:Monitor CPU usage, memory usage, HTTP request durations, Alert you if the error rate is high, Help you analyze trends and optimize performance

Q. Different types of metrics?

    1. counter: Measuring things that only increase  (You're counting events over time, and that number keeps going up, it never goes down.). eg: Number of requests, errors, jobs completed
        Rate of Increase= New Value−Old Value/Time interval    eg: At 2:00 PM, counter = 100, At 2:05 PM, counter = 160 ,  Rate = (160 - 100) / (5 min) = 60 / 300 sec = 0.2 per second

    2. Gauge: A metric that can go up or down over time. Tracking values that fluctuate, like memory usage, CPU usage, or temperature.

    3. summary: a Summary is a metric type used to track the distribution of events, such as request durations or response sizes.A Summary helps you: Measure how long something took (like a request duration), Calculate quantiles (like the 95th percentile),Track count and sum of observations.
        eg: http_request_duration_seconds_summary   -> tells Total number of requests, Total time taken by all requests, 95% of the requests were completed in under 0.4 seconds (as a quantile).
        Quantiles are ways to split data into equal parts.

    4.Histogram:  A histogram is a way of summarizing the distribution of numerical data by grouping values into ranges (called buckets or bins) and counting how many values fall into each bucket.
                  “How many data points fall into each range?”
                  
                  | Response Time (ms) | Count |
                  | ------------------ | ----- |
                  | 0–100              | 30    |
                  | 101–200            | 50    |
                  | 201–300            | 15    |
                  | 301–400            | 5     |  

                  This is a histogram: It has buckets: 0–100, 101–200, etc. And counts: how many requests fall into each range.
                  Buckets = predefined ranges.Each bucket has a count of how many values fall inside. helps visualize the distribution (spread and shape) of your data.

Q. metric collection and promql
           Metric collection is the process of gathering data about how your system is performing. Tools used: Prometheus, Grafana, etc.
           PromQL is the language used to query metrics stored in Prometheus.up – shows if targets are up/down. http_requests_total – total HTTP requests. rate(http_requests_total[5m]) – rate of HTTP requests over the last 5 minutes.


           requirements of metrics data
             MUST- 
                      1. target applications SLI - Metrics must help track the health and performance goals of your service (like uptime, latency, etc.)Example:If you want your app to respond within 1 second → track http_request_duration_seconds
                      
                      2. every component must inclucde perform metrics-Each part (like frontend, backend, DB) must expose how it’s performing.Why? So you can pinpoint where the issue is.
                      
                      3. info metric -  Include static info (version, build time, environment).
                      
                      4. mind cardinality - Cardinality = number of unique label combinations for a metric.⚠️ High cardinality (too many labels like user_id, session_id, etc.)= High memory usage + Slower queries. Keep labels simple and limited.
​
Q.NOde Exporter?
           Node Exporter: Exposes system-level metrics (CPU, disk, memory) for Prometheus to scrape.
           "Scrape" = collect metrics from a source (like Node Exporter) by pulling the data regularly.
           scrape=collect

Q. imp:
           prometheus is collecting the data and giving to grafana and grafana shows this in dashboards.

Q. SRE requirements for the whole observability stack?

<img width="1662" height="658" alt="image" src="https://github.com/user-attachments/assets/96866f4d-05eb-49a4-88cc-f57b44123c31" />

<img width="1305" height="422" alt="image" src="https://github.com/user-attachments/assets/75ff090a-c10e-4386-a826-f52163ce1c54" />

Q. Key Alerting Parameters in SRE?
           1. Precision:How accurately the alert detects a real problem. You don’t want false alarms (false positives) or missed problems (false negatives). High precision = fewer false alarms.
           
           2.Detection Time: How quickly an alert is triggered after a real issue starts.If your app goes down at 10:00 AM and the alert fires at 10:01 AM, detection time is 1 minute.
           
           3. Reset Time:Time taken to resolve or turn off the alert after the issue is fixed.You don’t want an alert to stay active once the problem is gone.

           4. recall: How complete your alerting is.Are you alerting every time there's a real issue?Reduce false negatives (missing alerts when something is wrong).Suppose your service crashes sometimes, but no alert is triggered.
That’s low recall — because the system didn’t catch the issue.


Q. SLO-Based Alerting with Prometheus

To show how we can use Prometheus metrics + PromQL + Grafana to define, trigger, and visualize alerts based on SLOs (Service Level Objectives).
Fulfillment Processor App: Demo app generating metrics.

                      Prometheus: Collects metrics and triggers alerts.
                      
                      Grafana: Visualizes metrics and alert status.
                      
                      Docker Compose: Manages multiple app instances.
                      
                      Alerting Rule: Based on error rate from the app.
fulfillment_document_requests_count_total: Total documents processed (with label document_status = success or failed)

Custom metrics:

fulfillment_document_errors: Sum of errors

fulfillment_document_total: Sum of all requests (success + failed)

<img width="946" height="233" alt="image" src="https://github.com/user-attachments/assets/bc45219e-6b86-4fbd-8844-9084dfbf5323" />
           This PromQL expression checks whether the error rate (failures divided by total requests) is greater than 0.001 (or 0.1%).
           The alert fires when more than 0.1% of requests are failing.
           The part in the pink box is > 0.001, which is the threshold for triggering the alert.

This is your SLO threshold for error rate.

(rate(document_errors[5m]) / rate(document_total[5m])) > 0.001   = This PromQL alert rule checks the error rate of your application over the past 5 minutes, and triggers an alert if the error rate is greater than 0.1% (i.e. > 0.001).
           trigger: When error rate > 0.1%

           SLI: Error rate
           
           SLO: Error rate should stay under 0.1%
           
Testing the Alert:
           Instance 1: No errors
           
           Instance 2: 1% errors
           
           Instance 3: 10% errors (deliberately fails)
           
Instance 3 starts/stops in cycles, causing the overall error rate to spike above the threshold temporarily.

Result:
           Alerts fire correctly when error rate > 0.1%.
           
           Alerts resolve once error rate drops.
-------------------------------------------------------------------------
Q. why alerting strategies get complicated?
           1. previously its given that 
                      (rate(errors[5m]) / rate(total_requests[5m])) > 0.001  - “Trigger an alert if the error rate is more than 0.1% in the last 5 minutes.”
                      here are some problems.
                      there will be an alert if there is a small issue
                      SRE 's will get unimp alerts
           2. why SRE's dont want these alerts:
                      SRE teams don’t want alerts unless something is seriously affecting the system.
                      Alerts should protect the error budget (the amount of errors allowed over time).
                      If we alert too early or too often, we annoy people without helping.
                      If we alert too late, we might miss serious problems.

           3. error budget?
                      Suppose your SLO is 99.9% success over 28 days.
                      If you process 7 million requests, you're allowed up to 7,000 errors.
                      That’s your error budget.
                      A big error spike happens: 5,000 errors.
                      A small error trickle happens later: 2,500 errors.
                      If you catch both on time, you're under budget = ✅ All good.
                      But if your alerts come too late, those same incidents might add up to over 7,000 errors = ❌ SLO breached = Change freeze (no new releases allowed).
                      
           4. What’s the Solution? Use Burn Rate
                      Instead of just looking at the error rate, we look at how fast we’re using up the error budget. That’s called the burn rate.
                      If burn rate = 1 → You're exactly matching the error budget.
                      If burn rate = 3 → You're using errors 3x too fast.
                      If burn rate = 10 → Budget will be gone in 3 days!
                      
           5. Smart Alerting Strategy
                      Use multiple burn rate windows to decide:
                                 When to page immediately (e.g., burn rate 14 over 5 minutes = fire page!)
                                 When to just log a ticket (e.g., burn rate 2 over 1 hour)
                      This gives:
                                  Good precision: alerts only when needed
                                  Good detection time: fast enough when it matters
                                  Good reset time: clears when issue is fixed
                                  Good recall: catches all serious problems
                                   
           
                      Burn rate = how quickly you're burning the allowed errors

--------------------------------------------------------------------
Goal of the Demo
To build smarter alerting rules using Prometheus that:

           Don't alert too quickly or unnecessarily (good precision)
           
           Don’t miss real problems (good recall)
           
           Alert on time (good detection time)
           
           Stop alerts once fixed (good reset time)
           
What's Happening in the Demo
           The team (Nina & Aiden) is using a demo app that simulates errors.
           
           They visualize and monitor error rates over different time windows (5m, 10m, 30m, 1h, etc.) using Grafana.
           
           Prometheus scrapes the data, evaluates alerting rules, and fires alerts when needed.

Types of Alerts:
1. Page Alert (Severity 1): Triggered when there's a spike in errors.
           Example Rule:

                      Burn rate > 14.4 over 5 mins and 1 hour
                      
                      OR burn rate > 6 over 30 mins and 6 hours
                      
                      ⚠️ Meant for urgent, short-term problems needing immediate SRE action.
   
2. Ticket Alert (Severity 3): Triggered for lower error rates but over a longer time.

Example Rule:

           Burn rate > 3 over 2 hours and 24 hours
           
           OR burn rate > SLO (0.1%) over 6 hours and 3 days
           
           📩 Meant for less urgent, long-term issues — creates tickets.

 Why Use Different Time Windows?
            Catch fast-breaking incidents (short windows like 5m + 1h)

           Catch slow-building issues (long windows like 6h + 3d)
           
           Avoid false alerts from tiny spikes that go away quickly.
           
Nina improved alerts by pre-calculating metrics like error rate over time windows.This lets Prometheus rules stay clean and understandable.Different types of issues trigger different alerts (pages vs. tickets).This smart setup helps balance alert fatigue vs. missing real problems.

Q. What is FailureFactor?
It’s a simulated error rate — used to inject controlled failures so you can test alerting, monitoring, and error-handling logic.
           Observability__Metrics__FailureFactor: 0.001 
"Generate failures at a rate of 0.1% of total requests."To test how your system reacts to different levels of failure.


Q.   Why Good Alerting Rules Matter
           Setting up alert rules is tricky.
           If alerts fire too often (false positives), the SRE team becomes overwhelmed or ignores them.
            So the alert parameters must be tuned to only fire when there’s a real, actionable problem.
            
Q. opsgenie and pagerduty?
            Opsgenie or PagerDuty to create tickets or pages depending on severity.
            Opsgenie and PagerDuty are key tools for managing system alerts and incidents. They automatically receive alerts, determine their urgency, and then send critical "pages" or create follow-up "tickets." This ensures the right on-call team members are quickly notified, streamlining responses and reducing downtime.

Q.  How Good Alerting Rules Work?
A good alerting rule:

           Checks the average error rate over two time windows:
           A long window (e.g. 1 hour) → gives good recall (it sees all real problems).
           A short window (e.g. 5 minutes) → gives good precision (makes sure the issue is still happening).
           ➡️ The alert only fires if the error rate is high over both windows.
This combination:
           Avoids false alerts (for issues that already resolved).
           Triggers quickly enough on real problems.
           Stops firing quickly once things are better (good reset time).
Burn Rate-Based Alerting:
           Burn rate = how fast you're using up your SLO error budget.
           Example:
           If your SLO allows 0.1% errors (99.9% success), and you're running at 1% error rate, you're burning 10x faster than allowed (burn rate = 10).
 Severity 1 (Page Now):
            Trigger an urgent alert (Severity 1) if:
           Burn rate > 14.4 over the last 1 hour AND 5 minutes
           Burn rate > 6 over the last 6 hours AND 30 minutes
           These indicate serious issues consuming the error budget too fast — someone needs to jump in now.
 Severity 3 (Ticket)
           Trigger a lower-priority alert (Severity 3) if:
           Burn rate > 3 over the last 24 hours AND 2 hours
            Burn rate > 1 over the last 3 days AND 6 hours
           These are less urgent, but still real issues — worth tracking, but don’t wake someone up.
Using this method ensures:

           High precision (alerts only when needed)
           High recall (detects real issues)
           Reasonable detection time (not too fast, not too slow)
           Good reset time (stops alerting once fixed)
