## Learning link

you can follow below courses under this link - 
https://learn.newrelic.com/page/courses


* Onboarding with New Relic
* Introduction to Observability
* Introduction to the Platform
* Introduction to Performance Monitoring
* Introduction to APM 360
* Database Performance Monitoring
* Introduction to Logs
* Introduction to Synthetics
* Configuring Application Observability
* Introduction to NRQL & Dashboards
* Introduction to Digital Experience Monitoring
* Introduction to Alerts
* Introduction to Distributed Tracing


** How to sent data to newrelic without agent? **
- MELT : metrics, events, logs, traces 
- MELT can be sent to newrelic by using api end point without agent if its  coming from a source that is not application or host.
- Also can use OpenTelemetry (OTLP collector)


To add agents:
- see the Integrations and agents on left side.
- then select guided install (good one) : install the infrastructure agent on your host and automatically instruments applications, logs, services on that hosts
<img width="1918" height="879" alt="image" src="https://github.com/user-attachments/assets/571ea4a8-c9fd-45f4-a691-9415872deb57" />

