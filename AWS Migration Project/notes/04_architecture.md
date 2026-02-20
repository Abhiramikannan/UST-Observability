ARCHITECTURE
-----------------------------
<img width="1571" height="1029" alt="image" src="https://github.com/user-attachments/assets/930cffa1-724d-4208-a412-c0822259cc1d" />



 Architecure changed to poll every 15 mins to perform DescribeHost API call along with eventBased. why?
---------------------------------------------------------------------------
1. Merin Replied like this: the utilization of host will change and it is not related to events so to cover that we need polling, for polling the lambda will call only DescribeHosts api
2. Host utilization means: How much of the dedicated host capacity is currently used.
3. Host utilization can change WITHOUT any CloudTrail event happening.
4. CloudTrail events happen only when: Infrastructure action occurs.
5. eg: Instance launched, Instance terminated, Host allocated, Placement changed
6. But utilization can change even when none of these happen.
7. real eg: Instance already exists, the load inside instance(application) increase,Host available capacity changes,utilization changes,No AWS lifecycle event happened


 What Happens If We Use ONLY Event-Based Lambda?
 -----------------------------------------------------------------
    1. Lambda runs only when event happens.
    2. Utilization changes without event → Dashboard becomes outdated

Eventbridge Rule
-------------------------
1. Target will be lambda
2. 15 mins lambda triggering using crone like schedule: the utilization of host will change and it is not related to events so to cover that we need polling, for polling the lambda will call only DescribeHosts api
