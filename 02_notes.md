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


  04/08/2025
  
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

13. Monitoring and Alerting?

        1. monitoring automatically tracks how a system is doing, which is key for keeping it reliable

        2. Alerting:  Triggers notifications when specific conditions are detected. Differentiates between two types of alerts:

                              Page: Requires immediate human response.
                              
                              Ticket: Requires a human to take action, but not immediately.
    
        3. Involving Humans: Only when the SLO is threatened ..it involves humans otherwise tools does this.
    
                                   "Humans should never watch dashboards, read log files, and so on just to determine whether the system is okay." This suggests a reliance on automated alerting to signal problems, rather than manual                 continuous observation. people should only get involved when there's a real problem, not constantly check everything manually.

14. Demand Forcasting and capacity Planning?

    <img width="605" height="392" alt="image" src="https://github.com/user-attachments/assets/3c88df1f-c78f-48de-8e37-680883ea2e16" />

    Demand Forcasting : Predicting how much traffic or usage your system will get in the future.If you know how many users or requests are coming, you can prepare your system to handle it.

    Capacity Planning: Making sure you have enough resources (servers, bandwidth, CPUs, memory, etc.) to handle the predicted demand.

15. Efficiency and performance?

          capacity can be expensive -> optimize the use
              EG:  when the traffic increases, we add more memory,servers...-> leads to higher cost..So instead of just adding more, SREs try to: Optimize existing resources (make better use of what’s already running), Avoid waste (idle servers, overprovisioned memory, etc.)

          Resource use -> function of demand(load), capacity, software efficeiency.

          Performance = How fast or well your system works. 
          Efficiency = How smartly you use your resources to maintain that performance

16. How SRE monitors utilization and performance?

          A regression is when something that was working fine earlier breaks after a new update or deployment. eg: Yesterday, the website was fast.Today, after a new release, it’s slow or crashing. That’s a performance regression.

          How Different Teams Handle Regressions:

              1. mature team: detect the regression, roll back the bad deployment, use monitoring tools to point the issue, release later after fixing.
    
              2. Immature team: May not have proper rollback pipelines. Dont detect issues quickly,Instead of fixing the code, they might: Add more CPU/memory, scale up servers,  They mask the problem by adding more resources instead of solving it.


CHANGE MANAGEMENT:

17. CHANGE  MANAGEMENT?

               means: how you handle updates to a live system.
        1. Changes cause most problems: About 70% of system failures happen because of changes made to the live system.

        2. How to fix it (Mitigations):
    
                    1. Roll out changes slowly: Don't release everything at once; do it step-by-step (progressive rollouts).

                    2. Find problems fast: Be able to quickly and accurately see when something goes wrong.
                      
                    3.  Undo changes safely: If there's a problem, be able to easily and safely undo the change.
    
       3. Use automation to avoid human mistakes:

                Let computers handle the changes instead of people.

                This helps to:
                
                      Make fewer mistakes.
                      
                      Prevent people from getting tired and making errors.
                      
                      Speed up how quickly you can make changes (improve velocity).
    



18. Pursuing maximum change velocity?

          which means how fast you can make and implement changes to your system. The core idea is that you shouldn't aim for perfect reliability (100%), but rather for a balance between reliability and how quickly you can develop and deploy new things.
      
     1. "100% is the wrong reliability target for basically everything"

                  It's unrealistic and often unnecessary to try to make a system never fail.
                  
                  Instead, you should:
                  
                          Decide how reliable your product needs to be: What level of uptime or performance is acceptable for your users and business?
                          
                          Don't overdo it: Don't spend extra effort and resources trying to make it more reliable than what's actually needed. This is inefficient.

      2. "Spend error budget to increase development velocity"

                An error budget is like an allowance for mistakes or downtime. It's the acceptable amount of unreliability you've decided on (e.g., if you aim for 99.9% uptime, your error budget is 0.1% downtime).
                
                The point is:
                
                        Don't aim for zero problems: The goal isn't to never have an outage. The goal is to make changes as fast as possible while staying within your allowed error budget.
                        
                        Use your error budget wisely: You can "spend" this allowed downtime or error allowance on things that help you develop faster, such as:
                        
                        New releases: Pushing out updates quicker, even if there's a small risk.
                        
                        Experiments: Trying out new features or approaches, which might occasionally cause minor issues but lead to innovation.

  19. Provisioning?

          Change management + capacity planning

      Change Management: How you make changes to your system.

      Capacity Planning: Figuring out how much resource (like servers, storage) your system needs.

      It specifically involves:

            Making existing services bigger: For example, giving an existing server more memory or CPU, or increasing the capacity of a service in a particular data center.
            
            Starting new services or locations: For instance, launching entirely new servers, setting up a service in a new geographical region, or adding more copies (instances) of an application.

      Why it needs to be done quickly:

            Cost of unused resources: If you have servers or other resources sitting idle that you've already paid for, it's a waste of money. So, you want to provision just what you need, when you need it, to avoid unnecessary costs.

     Why it needs to be done correctly:

          New capacity needs testing: Whenever you add new resources or expand existing ones, you must test them to make sure they work properly and integrate well with the rest of your system.

          It's often risky: Provisioning frequently involves making big changes to how your system is set up (configuration changes). These changes can easily introduce errors or problems if not done carefully, making it a potentially risky operation.

    In short: Provisioning is about getting your system the right amount of resources (like servers) at the right time. You need to do it fast to save money, and you must do it accurately because incorrect setup can cause big problems.



20. Emergency Response?

          1. dont be panic
          2. troubleshoot and fix
          3. if u feel overwhelmed, pull in more people.

21. Incident & postmortem thresholds?

        when a problem in a system becomes a formal "incident" that requires a deep dive analysis (a "postmortem").

        An incident is a serious problem with a system, and a postmortem is a detailed review of that incident to understand what happened and prevent it from recurring.

        setting up a threshold or conditions , if it meets the threshhold ->  you have an incident and need to do a postmortem.

        These conditions are:

                    Users see the problem: If users experience downtime or the system performing noticeably worse than usual, and this goes beyond an agreed-upon level (e.g., more than 5 minutes of slow response).
                    
                    Data is lost: Any instance where data is permanently lost, no matter how small. This is a very critical threshold.
                    
                    Engineers had to do major work: If an on-call engineer had to step in and perform significant, emergency actions to fix the problem, like rolling back a software update, or redirecting all user traffic away from a broken part of the system. This indicates a serious issue.
                    
                    Problem took too long to fix: If the time it took to resolve the issue (from detection to full recovery) exceeded a predefined acceptable limit.


22. Postmortem philosophy?

          "Postmortem philosophy" and is about the purpose and approach to conducting a postmortem.

          A postmortem (also called a post-incident review or root cause analysis) is a structured process that happens after a significant problem or incident has occurred and been resolved in a system (like a website going down or an application crashing). It's not about blaming anyone, but about learning and improving.

          The primary goals of writing a postmortem are to ensure that:
                  
                  The incident is documented: This means formally recording all the details about what happened, when, what was affected, and how it was fixed. This record serves as a history and a reference for future issues.
                  
                  All contributing root causes are well understood: This is the most critical part. It's about digging deep to find all the underlying reasons why the incident happened, not just the immediate cause. For example, if a server crashed, the root cause might not just be "server crashed," but why it crashed (e.g., a software bug, an incorrect configuration, insufficient memory, a human error in deployment).
                  
                  Effective preventive actions are put in place to reduce the likelihood and/or impact of recurrence: Once you understand the root causes, the next step is to figure out what specific actions you can take to prevent the same problem from happening again, or at least to minimize its impact if it does. These actions could be anything from fixing a bug, improving a process, adding more monitoring, or providing more training.
                  
                  Postmortems are expected after any significant undesirable event:
                  
                  This means that whenever something goes seriously wrong with the system, a postmortem should be a standard practice. It's part of the standard operating procedure for handling major problems.
                  
                  Writing a postmortem is not a punishment: This is a crucial philosophical point. The postmortem process should be blameless. The goal is not to find who to blame, but to understand the system and process failures. If people fear punishment, they won't share full information, which defeats the purpose of learning and preventing future incidents


Blamelessness:  "Blamelessness" means when problems happen, focus on fixing system issues, not on blaming individuals. Everyone involved is assumed to have good intentions. This approach encourages open reporting of problems, helping the team learn and improve without fear.

23. "Toil management/operational work?

        Toil: Toil refers to a specific type of work directly involved in keeping a service running, and it has several key characteristics:

                  1. Manual: requires human, not automated

                  2. Repetitive: It's work that you do over and over again, like every day, or for every new customer. It's not a one-time task.

                  3. Automatable: This is crucial. While it's currently manual, it could be automated because it doesn't require complex human judgment or creativity.

                  4. Reactive & Firefighting: It's work you do because something happened (like an alert going off or a user complaining), not work you planned ahead to make things better. It's like constantly putting out small fires.

                  5. No Lasting Improvement: This work doesn't actually make the system stronger or prevent future problems. It just fixes the immediate issue. (Think of patching a leaky bucket instead of getting a new one.)

                  6. Grows with the System: The more users or parts your system has, the more of this tedious work you'll have to do. It's not efficient.

      Why we still do some "Toil":

                1. Learning by Doing: When you manually deal with problems, you learn exactly how the system breaks. This helps you design much better systems later.

                2. Can't Automate Everything: Some tasks are too complex or rare to automate perfectly. Humans are still needed for unique situations.
            
                3. Know What to Automate: By doing these manual tasks, you see patterns and discover which tasks are the most annoying or frequent. This tells you exactly what to prioritize for automation to save the most effort.

24. How SRE helps make cloud services reliable ?

    SRE helps make cloud services reliable by:

* **Growing smart:** As your system gets bigger, the amount of manual work to run it shouldn't explode.
* **Automating everything possible:** Use computers to manage growth, not just hiring more people.
* **Working together:** Make sure the teams building new things and keeping them running work as one.
* **Balancing speed and stability:** Use an "error budget" to know how much downtime is okay, so you can release new features faster without breaking everything.
