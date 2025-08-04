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
   
3. 5 Key Areas of DevOps. SRE implements Devops
   
         1. Reduce Organizational Silos: Instead of working separately, all teams work together with shared goals.
         2. Accept Failure as Normal: Focus on recovering quickly and learning from failures.
         3. Implement Gradual Changes: Make small changes. Small changes are easier to test, fix, and release.
         4. Leverage Tooling and Automation: Use tools to automate repetitive tasks like: Deployment, Monitoring, Infra
         5. Measure Everything: Track everything using metrics:->App performance, Deployment time, Error rates, System health.

4. SRE approaches to Operations:
   
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



5. What do SRE teams do?
   
   SRE (Site Reliability Engineering) teams are responsible for making sure that systems, services, and applications are reliable, scalable, and efficient.
   
   1. Monitor Systems and Services:
      
      Set up real-time monitoring and alerting systems

      Use tools like Prometheus, Grafana, Azure Monitor, Datadog, etc.

      Keep track of latency, traffic, errors, uptime, and saturation
      
    2.  Automate Operations

      write scripts or use tools to automate repetitive manual tasks
  
      Example: auto-scaling, backup, log rotation, restarting services
  
      Tools: Bash, Python, Terraform, Ansible, Jenkins, etc.
    
    3. Set and Track SLOs/SLIs/SLAs

       Define SLOs (Service Level Objectives) like "99.9% uptime"
  
       Measure SLIs (like latency, error rate)
  
       Ensure systems meet SLAs (agreements with customers)

    4. Improve System Reliability
    5. Support CI/CD Pipelines
    6.  Ensure Security and Compliance
  
  6. What are the Key features of SRE?
     
           1.  Not Everything Has to Be Perfect: They focus on keeping services good enough while still allowing new features to go live.

           2.  Set Clear Goals for Reliability (SLO & SLI):
                       SLI (Service Level Indicator): What you measure (like uptime, speed, errors).

                       SLO (Service Level Objective): The target you want to reach (like “we want 99.9% uptime”).
     
           3.  Error Budget:
                     Think of an error budget like your "allowed limit" for mistakes or downtime.
     
                      Example:  Your goal (SLO) is 99.9% uptime. So you are allowed to be down for 0.1% of the time (about 43 minutes per month). That 0.1% is your error budget

                      if you stay within the budget: u can release new features , else :  Stop new changes and fix the system first.

           4. Automate Repetitive Work (Toil):

                   SREs don’t like doing the same boring manual tasks again and again.

                  So they write scripts or use tools to do it automatically.
                  
                  Example: Restarting servers, checking logs, deployments.

          5. Keep an Eye on Everything (Monitoring):

                     SREs build dashboards and alerts to know:

                          Is the website slow?
                          
                          Is something broken?
                          
                          This helps fix issues before users even notice.

          6.  Learn from Mistakes (Blameless Postmortems)
                               
                    If something breaks, they don’t blame anyone.
                    
                    Instead, they write down what happened, why, and how to fix it.
                    
                    Everyone learns and improves from the mistake.
            
7.  What is SRE,SLI,SLO,SLA?
       
         SRE (Site Reliability Engineering) is a role or team that:

                  Makes sure systems (like websites or apps) run reliably
                  
                  Fixes problems before users see them
                  
                  Uses coding and automation to manage infrastructure and systems
                  
                  Think of SREs as engineers who keep things running smoothly.

    SLI:
        It is a metric that tells how well your system is working.
        Example: % of requests with no errors, or % of time the website is up.
        “How often was the service successful?”
        This number comes from monitoring data.

                  🔧 Format: Function(metric) < threshold
                  Example: error_rate < 0.01 (i.e., <1%)
    
         An SLI is a measurement of how well a system is working.

                  Examples:
                  
                  Website uptime
                  
                  API response time
                  
                  Error rate
                  
                  👉 It's the actual number you measure.
                  
                  Example:
                  
                  "Our website was up 99.92% this month." → That’s the SLI
    SLO:
        This is a goal based on the SLI. SLO = a goal or target for how well a service should perform over time

        It tells what level of service you want to provide.
        eg: “We want 99.9% of requests to succeed every month.”
        SLO = SLI + goal
                      So:
                      If the SLI is measuring uptime →  Your SLO could be "99.9% uptime in 30 days"

      An SLO is a goal you set based on your SLIs.

                Example:
                
                "We want the website to be up 99.9% of the time every month."
                
                That’s your target or promise to yourself.
                If your SLI is lower than your SLO — you’re not meeting your goal.

    sum(SLI met) / time window >= target %

        meaning: If you're measuring successful responses in a 30-day period:

                  Out of 1,000,000 requests, 999,000 were successful →
                  Your SLI is 99.9%
                  
                  ✅ So if your SLO is 99.9%, you've met your target.

    “Try to exceed SLO target, but not by much.”

        Why not too much?
    
        Because if your system is always way better, then maybe your goal is too easy and you're not innovating enough (wasting potential error budget).

    How to Choose a Good SLO?

      Don’t try for 100% perfection (it’s unrealistic and costly)

      Avoid strict “always” or “never” rules

    Why Does It Matter?
                Sets priorities
                
                        Helps teams (Dev + SRE) know where to focus effort
                        
                        If you're close to SLO limits, slow down releases and improve reliability
                
                Sets user expectations
                
                        Customers know what level of performance to expect


SLA:

    An SLA is a formal agreement with your customers. It includes the SLO + some margin and penalties if you break it.

              It says:
              
              “We promise to keep your service up 99.9% of the time, or we’ll give you a refund.”
              
              SLA is legally binding
              
              It's based on your SLOs
              
              Usually used between companies and clients
                SLA= (SLO + margin) + consequences = SLI + goals +consequences

9. How to measure reliability?

         1. availability = Good time/Total time

         2. handles distributed request/response services

10. What is an Error Budget?

        "Error budget = how much failure is okay."

    1. SRE + Product Team set a target (example: “System must be available 99.9% of the time”)

    2. 100% - 99.9% = 0.1% error budget
        
           That 0.1% is the allowed downtime or failure

          For example, around 43 minutes per month

    3. Monitoring checks real uptime
   
                If the site is down for 20 minutes → you're still okay

                If it goes beyond 43 mins → you're over budget
       
     4. Control loop: Based on usage, teams decide whether to slow down or speed up releases
  

  11. Why is the Error Budget Useful?

| 🟧 Point                             | 🔍 Simple Meaning                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| ✅ **Common incentive for Dev & SRE** | Devs want to release fast. SREs want reliability. Error budgets help them agree.      |
| ✅ **Dev team can manage risk**       | Developers decide when to release based on how much budget is left.                   |
| ✅ **Stops unrealistic expectations** | You don’t have to aim for 100% uptime (which is very hard and expensive).             |
| ✅ **Dev team becomes self-policing** | They are more careful about what they deploy, because failures reduce their budget.   |
| ✅ **Shared responsibility**          | If infrastructure fails, both Dev and Ops share the impact — not just blame one team. |


  Imagine your app should be up 99.9% of the month (SLO).

  That gives:

    ⏱ 43 minutes of acceptable downtime per month (Error Budget)
    
    If the app crashes for:
    
    🔹 10 mins → you’re still safe (can deploy new features)
    
    🔹 50 mins → over budget (stop releasing new changes until it's stable again)

  12. PRODUCT LIFECYCLE?
      
      <img width="1384" height="723" alt="image" src="https://github.com/user-attachments/assets/d98010d7-118d-4fe2-af54-2aa71c930798" />



   


