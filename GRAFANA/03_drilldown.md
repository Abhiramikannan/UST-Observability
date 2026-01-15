Drilldown from Stat panel to Table
------------------------------------------------------
  1. If table contains status like Unhealthy, Healthy
  2. U want to Show healthy details when u select healthy from stat panel
  3. U want to show Unhealthy details when u select Unhealthy from stat panel.
  4. In stat panel -> Just change the data link (Nthg else)
  5. In table panel -> Add transformation ->filter data by values -> status equalto Variable u created.(status)

Variable creation:
-----------------------------
1. Always give variable as same as ur fieldname
2. My csv data of table contains 2 status: HEALTHY, UNHEALTHY
   <img width="1120" height="574" alt="image" src="https://github.com/user-attachments/assets/555b71ca-e8b8-4d45-8ec3-6a29c18e3fd1" />


Screenshots of Healthy Drilldown:
-----------------------------------------------

table panel:
<img width="1525" height="227" alt="image" src="https://github.com/user-attachments/assets/d051befa-751b-4b6d-8bb4-efd4f5d2a36a" />

stat panel: Give the status=HEALTHY(LOOK CSV DATA)(U want healthy details only here , thats y)
<img width="1601" height="477" alt="image" src="https://github.com/user-attachments/assets/e2090713-48f6-4ac7-93b9-2eeef3442721" />

So this works


------------------------------------------
scenario of drilldown level 2(Table to table)
-----------------------------------------
here, when i select particular hostname from table it shows the details of that host in next table:
<img width="1737" height="489" alt="image" src="https://github.com/user-attachments/assets/38385c39-ab4e-412c-aceb-8efe08a4297c" />

the details should be shown in level 3:
<img width="1874" height="343" alt="image" src="https://github.com/user-attachments/assets/57f83ecf-90ce-45c6-a110-038c74e7b187" />

**Steps:
variable creation:
<img width="1066" height="684" alt="image" src="https://github.com/user-attachments/assets/3d4f01ba-f535-4d8e-a415-a21c837d070a" />

1. edit the level 3 panel and add the transformation
<img width="1554" height="243" alt="image" src="https://github.com/user-attachments/assets/41164f5f-01e3-448c-9bed-bc3c3e4a9beb" />

2. edit the level 2 panel(table) where  u want to click:
   <img width="1459" height="573" alt="image" src="https://github.com/user-attachments/assets/6f8b5c67-8589-4c31-8ffc-49bf501d932d" />

So this will work.


-------------------------------------
Scenario of drill down from level 3 to level 4
-----------------------------------------------
I want to implement drill down based on the error type of particular host(so 2 variables should be used in transformation)

aim:
<img width="1890" height="232" alt="image" src="https://github.com/user-attachments/assets/2d7379cb-d336-4b15-bdea-e95555937c8c" />
<img width="1915" height="244" alt="image" src="https://github.com/user-attachments/assets/36705007-1764-4779-a997-113bf8ede95a" />

solution:

variable:
------------
<img width="1178" height="617" alt="image" src="https://github.com/user-attachments/assets/8505cf99-ad0f-4ab3-b4c8-953ed3cb670f" />

1. take the level 4 panel and add transformation: USE MATCH ALL -which matches both conditions - otherwise wont get
<img width="1268" height="347" alt="image" src="https://github.com/user-attachments/assets/db0c0d32-d179-44f3-a2b5-9db3e100407c" />

2. In level 3 panel:
   <img width="1465" height="457" alt="image" src="https://github.com/user-attachments/assets/2134b8d3-45a7-4925-a4f6-187eedca0c4e" />

so this will work

   














