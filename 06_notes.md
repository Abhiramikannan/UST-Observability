11/8/25
link: https://grafana.com/go/webinar/intro-to-alerting-with-grafana/?pg=tutorials&plcmt=results
1. IRM:IRM simply means Incident Response Management (sometimes called Incident and Request Management in ITSM). It’s the process of:

                  Detecting when something goes wrong in a system or service.
                  
                  Responding quickly to fix it.
                  
                  Documenting what happened and how it was resolved.
       
       

   ------------------------------------------------------------------------------
   
2. REACTIVE ALERTING VS PROACTIVE ALERTING VS PREDICTIVE ALERTING:

     REACTIVE ALERTING: after the issue already occured. It will let u knw somethg is broken ,go and fix that. eg: A server CPU hits 100% and the system sends an alert.
     Users are already experiencing slowness when you get the notification.(Grafana Alerting : sent alerts when met the conditions like cpu % >90)

     PROACTIVE ALERTING: It will let u know before the particular issue becomes major problem.
                         Catch early warning signs to prevent failures.Example: Alert triggers when CPU usage is steadily above 80% for 10 minutes. You have time to scale resources before it reaches 100%.( Error Budget & SLO Alerting: slo warns when u r burning ur error budget quickly)

     PREDICTIVE ALERTING: Use historical patterns + AI/ML to predict an upcoming issue.Monitoring predicts memory will run out in 2 hours if usage keeps growing.
                           Sends an alert so you can fix it before it happens. Avoid incidents entirely.
                         eg: Your smart home predicts a high chance of fire tomorrow based on past cooking patterns.
                         Adaptive alerting → The system learns your normal patterns and automatically adjusts alert thresholds based on current trends.eg:If CPU normally runs at 10%, and suddenly jumps to 40%, it might alert you even though it’s below 90%, because that’s unusual for your system.


---------------------------------------------------------------------------


3. TIGHTLY COUPLING:
          2 systems closely linked
          If one changes, the other reacts immediately because they’re deeply integrated.
   
Q. Tight coupling between Observability and IRM means less toil and better insights. Why?

Tight coupling = Observability tools and Incident Response Management (IRM) tools are directly connected.

When there’s a problem, the observability tool automatically sends all the important data (logs, metrics, traces) to the IRM system along with the alert.

This means:

You don’t have to waste time hunting for data after the incident → less toil.

You get the full context of the issue immediately, so you can understand and fix it faster → better insights.
  
4. Handson:
links:

    https://grafana.com/tutorials/grafana-fundamentals/?pg=tutorials&plcmt=results
   
    https://grafana.com/tutorials/alerting-get-started-pt6/?pg=tutorials&plcmt=results
   
    https://grafana.com/tutorials/alerting-get-started-pt4/?pg=tutorials&plcmt=results
           
https://killercoda.com/grafana-labs/course/grafana/grafana-fundamentals


The goal is to learn:

      How to run ad-hoc (one-time) queries
      
      How to see how many requests your app is getting
      
      How to group that info in different ways
