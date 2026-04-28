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
2. AWS health events sent to default eventbus(automatically) and created a eventbridge rule to sent to cloudwatch log group in DH account 1.
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


Flow of this Architectural Solution:
-----------------------------------------------
1. 15 mins scheduled eventbridge rule for calling describehosts API . 
2. Eventbased trigger for aws health events and cloudtrail events.

15 mins trigger:
-------------------------
1. lambda will trigger every 15 mins to call describehosts API .
2. First Run of lambda: When the lambda is triggered for first time - fetch describehosts API and will get the host id and instances associated in the hosts.
3. With that Instance id we will call ADX end point and fetch the Tags(Application name and other tags) and eventname for all instances(output of describehosts).
4. The data after hitting adx can be mapped with instance id -> host id -> application name .
5. The mapping can be saved into s3 bucket in the files (application.json in application folder, instances.json in global.json).
6. This will be happening in first run.
7. 2nd run of lambda after the first trigger (next 15 mins) : It will call describehosts API and get host id and instances currently running .
8. s3 is having the instances and host id and application mapping from previous run.(First run is very imp for s3 mapping).
9. So the later the describe hosts output..the lambda compares the instances running currently(output from describehosts) with s3.
10. If any instances is missing from current output and s3 is having that - it means it is terminated or stopped. Then lambda will hit the instance id in adx and fetch the state and update the s3 accordingly.
11. If the state is stopped - s3 updated to stopped, if terminated - delete from s3.
12. If any instances are new in currently fetched describehosts, (compare s3 with current describehosts result to find new) , then hit adx and fetch details and update s3 accordingly.
13. The 2nd run logic will be applied to next every 15 mins runs.




