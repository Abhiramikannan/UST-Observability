Drilldown from Stat panel to Table
------------------------------------------------------
  1. If table contains status like Unhealthy, Healthy
  2. U want to Show healthy details when u select healthy from stat panel
  3. U want to show Unhealthy details when u select Unhealthy from stat panel.
  4. In stat panel -> Just change the data link (Nthg else)
  5. In table panel -> Add transformation ->filter data by values -> status equalto Variable u created.(status)

Variable creation:
-----------------------------
1. My csv data of table contains 2 status: HEALTHY, UNHEALTHY
   <img width="1120" height="574" alt="image" src="https://github.com/user-attachments/assets/555b71ca-e8b8-4d45-8ec3-6a29c18e3fd1" />


Screenshots of Healthy Drilldown:
-----------------------------------------------

table panel:
<img width="1525" height="227" alt="image" src="https://github.com/user-attachments/assets/d051befa-751b-4b6d-8bb4-efd4f5d2a36a" />

stat panel: Give the status as the value from table panel(U want only that , thats y)
<img width="1601" height="477" alt="image" src="https://github.com/user-attachments/assets/e2090713-48f6-4ac7-93b9-2eeef3442721" />

So this works

