DH OBSERVABILITY SOLUTION ARCHITECTURE
-------------------------------
<img width="2846" height="1407" alt="Latest architecture" src="https://github.com/user-attachments/assets/865bedd3-45e1-47ef-92ff-fed99876e564" />

What we are having?
-----------------------------------
1. Two Dedicated hosts account( dhm-prd, dhm1-prd)
2. Azure Data Explorer(ADX) - App accounts cloudtrail events(runInstances, startInstances, stopInstances, TerminateInstances) are available in ADX.

3 EventBridge rules in DH 1
---------------------------
1. 15 mins polling describehosts in both accounts(DH account 1, DH account 2) using Observability Lambda. DH account 1 needs lambda execution role and policy(permissions).
2. AWS health events sent to default eventbus(automatically) and create a eventbridge rule to sent to cloudwatch log group in DH account 1.
3. Event based rule for the cloudtrail events(Allocate Hosts, Release Hosts) to cloudwatch Log group.

Dedicated Hosts Account 2:(Only Read only access)
--------------------------------
1. The Dedicated Host utilization is fetched by calling  DescribeHosts API call by lambda from DH 1. (Cross account role required)
2. Aws health events from Dh account 2 is sent to the default event bus of Dh account 1, then sent to cloudwatch log group using eventbridge rule.(same eventbridge rule used for cloudtrail events forwarding)
3. The eventbridge rule is created in Dh account 2  to forward the cloudtrail events(AllocateHosts, ReleaseHosts) to DH account 1 default bus (bus policy required in DH 1 to accept the events).(event based)

LOG Groups:
-----------------------
1. Describe hosts : /aws/lambda/CCOE-Observability-Lambda
2. Aws Health events/ Maintenance events and Cloudtrail events(Allocate Hosts, Release Hosts) : /aws/events/dh-observability events


