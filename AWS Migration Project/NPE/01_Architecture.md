DH OBSERVABILITY SOLUTION ARCHITECTURE
-------------------------------
<img width="2846" height="1407" alt="Latest architecture" src="https://github.com/user-attachments/assets/865bedd3-45e1-47ef-92ff-fed99876e564" />

What we are having?
-----------------------------------
1. Two Dedicated hosts account
2. Azure Data Explorer(ADX) - App accounts cloudtrail events(runInstances, startInstances, stopInstances, TerminateInstances) are available in ADX.

3 EventBridge rules
---------------------------
1. 15 mins polling describehosts in both accounts(DH account 1, DH account 2)
2. AWS health events sent to cloudwatch log group.
3. Event based rule for the cloudtrail events(Allocate Hosts, Release Hosts) to cloudwatch Log group.


