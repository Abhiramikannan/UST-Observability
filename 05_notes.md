8/8/25
link: https://grafana.com/go/webinar/getting-started-with-grafana-dashboard-design/?pg=tutorials&plcmt=results

1.  What is K6?
 K6 is an open-source tool used for load testing and performance testing of web applications and APIs.
    
🔹 Use Case:
It helps SRE/DevOps/QA teams find out:

How fast is the system?

How much load can it handle before  breaking?

How does it behave under stress?

---------------------------------------------------------
2.  What is MTTD (Mean Time to Detect)?
MTTD is a metric used in observability and incident management.

🔹 Definition:
MTTD = Average time taken to detect an issue or failure after it occurs.

🔹 Formula:
MTTD = Total time taken to detect issues / Number of incidents

🔹 Why it's important:
Lower MTTD = Faster detection = Better reliability

Helps in identifying gaps in monitoring and alerting

-------------------------------
3. designing dashboard
-------------------------
1.  graph panel
2. browse data that collected so far
3. collect most imp lookin metric
4. repeat until profit
5. dashboard should either tell a story or answer the question.


-----------------------------------------
4. DASHBOARD DESIGN BEST PRACTICES:
-----------------------------------------
1. scan pages in z pattern - imp(top-left,top right),center-supportve data,bottom-less critical
2. size in dashboards: Use larger panels for key metrics
3. colours - to get attention 
4. shapes : circle -status indicators,rectangles-histogram/barcharts,triangle-change/alerts
5. colourcoding Grafana feature: Stat panels, Table panels, Gauge and Bar panels. Example: If CPU usage > 90%, show red; if < 50%, show green.

---------------------------------------
5. UX CONCEPTS OF OBSERVABILITY DASHBOARD:
-------------------------------------------
1. Logical grouping
       Quick Look – Key health indicators, Read Path – Metrics related to read operations, Write Path – Metrics related to write operations
   
2. data link feature of grafana - abnormal graphs:
              Allows clicking on a panel to navigate to related dashboards or logs.
              Helps investigate abnormal graphs quickly.

3. red  yellow green - most imp data
       Normal values (green/blue), Warning ranges (yellow), Critical values (red)

4. colours:  red-bad, blue-good , avoid combo of red and green'
-------------------------------------------------



6. choosing right metrics for your dashboard:
------------------------------------------------------

1. to monitor ur service - red method (req rates,errors, duration-latency)
2. use method (utilization,saturation,errors)-track infrastructure resources
3. 4 golden signals of monitoring -latency,traffic,saturation,error

-----------------------------
7. organized dashboards
----------------------
1. top down z pattern : humans scan-  Left to right, then down, left to right again — just like a “Z” shape. Put the most important panels (alerts, KPIs) in the top-left or center.
2. spacing b/w panels: Use white space or empty space to separate different sections.
3. padding: This is the space inside a panel between the panel's border and its content.Without padding, text or graphs look cramped. With proper padding, everything appears neat and structured.
4. transaparent bg: In Grafana, panels can have a transparent background (instead of a solid grey, black, etc.)Makes the dashboard look minimal and modern.



------------------------------
8. NOTES:
---------------------------
### 🔹 **Unannotated Panel vs Annotated Panel**

* **Unannotated Panel**: A panel that only shows the raw time series data (like CPU usage, memory usage) **without any context** or markers.
* **Annotated Panel**: Has **annotations or markers** that provide **contextual information** on the graph, like:

  * Deployment times
  * Outage events
  * Manual notes
    📌 Useful for correlating data spikes/drops with real-world events.

---

### 🔹 **Standard Time Series Panel vs Alternative Options**

* **Standard Time Series Panel**:

  * Shows metrics over time in **line graphs**.
  * Best for trends, anomalies, patterns.
* **Alternative Options**:

  * **Stat Panel** – shows a single number (e.g., CPU usage now)
  * **Gauge Panel** – shows a value in a dial format.
  * **Bar Chart**, **Pie Chart**, **Heatmap**, etc.
  * Choose based on **what insight you want** (single value, comparison, distribution).

---

### 🔹 **Library Panels**

* **Library Panels** let you:

  * Create **a reusable panel** design once.
  * **Copy and reuse** it across multiple dashboards.
  * If you update the library panel → all dashboards using it get updated too.
    ✅ Helps maintain consistency and reduces duplication.

---

### 🔹 **White Labeling**

White labeling allows you to **customize Grafana UI** to reflect your own brand (especially for enterprise or client demos).

Includes:

* **Standard Login**: Use your company’s login page, logo, and styles.
* **Custom Branding**:

  * Replace Grafana logo with your own.
  * Change color scheme and fonts.
  * Customize footer, menu text, etc.

🔒 **Requires Grafana Enterprise** (not available in open source).

---

### 🔹 **Grafana Play**

* **Grafana Play** is an **official live demo site** by Grafana Labs:

  * URL: [https://play.grafana.org](https://play.grafana.org)
  * Shows **sample dashboards** and **real-time data**.
  * You can explore various panel types, alerting, variables, and best practices.
  * Great for **learning** or trying out Grafana without setting it up locally.

---

Let me know if you want screenshots or a side-by-side comparison for any of these.

