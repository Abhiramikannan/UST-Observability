1/8/25

link: https://www.youtube.com/live/eopc_ijIfLg

SRE FUNDAMENTALS:

1. What is SRE?
SRE (Site Reliability Engineering) is a role and practice in tech companies where software engineers work on making systems more reliable, faster, and able to handle problems automatically.
The idea of SRE came up by Google.

SRE=middle role b/w development and operations

2. What is Devops?
  DevOps is not a tool or a single job — it’s a culture and set of practices that helps different teams in a company work together smoothly.
   It encourages collaboration between teams that usually work separately: Developers,Operations,Architecture,Networking.
   ...work separately (like they are in different "silos" or isolated rooms). That causes confusion, delays, and bugs.
   
3. 5 Key Areas of DevOps
   
         1. Reduce Organizational Silos: Instead of working separately, all teams work together with shared goals.
         2. Accept Failure as Normal: Focus on recovering quickly and learning from failures.
         3. Implement Gradual Changes: Make small changes. Small changes are easier to test, fix, and release.
         4. Leverage Tooling and Automation: Use tools to automate repetitive tasks like: Deployment, Monitoring, Infra
         5. Measure Everything: Track everything using metrics:->App performance, Deployment time, Error rates, System health.

5. SRE approaches to Operations:
   SREs treat operations like a software problem — they apply coding, automation, and metrics to make systems more reliable and scalable.
| Principle                          | Explanation                                                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Eliminate Toil**              | Repetitive manual tasks (like restarting services, checking logs) are automated using scripts, tools, or code.                                      |
| **2. Use SLIs, SLOs, SLAs**        | Reliability is measured clearly using: <br>🔹 SLI (Service Level Indicator)<br>🔹 SLO (Service Level Objective)<br>🔹 SLA (Service Level Agreement) |
| **3. Embrace Risk & Error Budget** | 100% uptime is not the goal. Small controlled failures are accepted within the “error budget.”                                                      |
| **4. Monitoring & Observability**  | SREs build dashboards, alerts, and traces to deeply understand how systems behave.                                                                  |
| **5. Automate Everything**         | From deployments to rollbacks to scaling — everything is automated through code.                                                                    |
| **6. Blameless Postmortems**       | After a failure, SREs do analysis without blaming anyone, to learn and prevent it in the future.                                                    |

| Traditional Ops         | SRE Approach                                    |
| ----------------------- | ----------------------------------------------- |
| Manual deployment steps | CI/CD pipeline auto-deploys code                |
| Fix issues manually     | Self-healing systems (auto-restart, auto-scale) |
| Wait for alerts         | Proactive monitoring and health checks          |

6. What do SRE teams do?
   SRE (Site Reliability Engineering) teams are responsible for making sure that systems, services, and applications are reliable, scalable, and efficient.
   1. Monitor Systems and Services:
      
      Set up real-time monitoring and alerting systems

      Use tools like Prometheus, Grafana, Azure Monitor, Datadog, etc.

      Keep track of latency, traffic, errors, uptime, and saturation
      
  2.  Automate Operations

     Write scripts or use tools to automate repetitive manual tasks

    Example: auto-scaling, backup, log rotation, restarting services

    Tools: Bash, Python, Terraform, Ansible, Jenkins, etc.
    
  3. Set and Track SLOs/SLIs/SLAs

     Define SLOs (Service Level Objectives) like "99.9% uptime"

     Measure SLIs (like latency, error rate)

    Ensure systems meet SLAs (agreements with customers)

  4. Improve System Reliability
  5. Support CI/CD Pipelines
  6.  Ensure Security and Compliance
   


