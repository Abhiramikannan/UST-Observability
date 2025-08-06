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


​
