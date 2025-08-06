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

