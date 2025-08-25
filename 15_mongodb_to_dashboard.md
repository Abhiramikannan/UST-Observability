TASK:
------------------------------------------
MongoDB:
      Shridhar to send an excel with data,
      Team to upload the excel to a cloud based Mongo instance,
      connect it with Grafana and then create some dashboards


---------------------------------------------------------
1. Saving the excel(database doesnt know how to  open it and whats inside) into csv (any database can read and understand)
      ---------------------------------------------------------------
<img width="1915" height="993" alt="image" src="https://github.com/user-attachments/assets/2fa138db-81a4-4810-8cdb-d0f204c4b653" />

EXCEL: contains raw data + unwanted information(formulas,formatting,charts)

CSV: raw data

-------------------------------------------------------------------------------------------
2. Create a mongodb atlas free account
      ---------------------------------------------------------------------------------------
3. create a cluster -aws choosen
   --------------------------------------------
   <img width="1901" height="913" alt="image" src="https://github.com/user-attachments/assets/b82804d7-1cf1-496b-908a-2d41fc995b4f" />
   <img width="1311" height="830" alt="image" src="https://github.com/user-attachments/assets/2a11de51-4a24-4702-8d9a-6f9f087c65b6" />
----------------------------------------------------------
4. Add data -> upload csv file
   --------------------------------------
   <img width="1477" height="704" alt="image" src="https://github.com/user-attachments/assets/0f2c5e57-fcee-4a78-b445-57c99ae57b9c" />
   <img width="1444" height="642" alt="image" src="https://github.com/user-attachments/assets/a26260a3-4d04-42d1-be21-54ae4cc8d3f7" />

   Import on compass -> take u to a page
   --------------------------------
   <img width="1203" height="887" alt="image" src="https://github.com/user-attachments/assets/01cff2d8-3728-43f4-bb91-099d83c82d87" />

   create the database user
   ----------------------------
         type the username and password and ->create database user
   <img width="1385" height="785" alt="image" src="https://github.com/user-attachments/assets/77ebf95d-3614-4bee-8a91-8648154519bb" />

   choose the connection method - choose compass
   -----------------------------------
   <img width="1629" height="920" alt="image" src="https://github.com/user-attachments/assets/4c4c493e-810c-4470-8560-dd4045372b1f" />

   select compass-> take u to a page
   -----------------------------------------
   <img width="1304" height="895" alt="image" src="https://github.com/user-attachments/assets/f5ca1b4e-bd62-4322-8751-797355c2f070" />

           copy download url: https://downloads.mongodb.com/compass/mongodb-compass-1.46.8-win32-x64.exe


   <img width="1755" height="761" alt="image" src="https://github.com/user-attachments/assets/c2d40d01-fd14-4d57-9457-5b27dfcaa532" />

--------------------------------------------------------------------
5. trying installing through company portal
   ----------------------------------------------------------------------
<img width="1446" height="788" alt="image" src="https://github.com/user-attachments/assets/81b0d99b-59ea-4648-96d9-4bcf8bca999d" />

Add new connection
---------------------------
      clusterts->connect->compass ->copy the connection string
      
      paste ur connection string in the uri

<img width="1487" height="759" alt="image" src="https://github.com/user-attachments/assets/19a0e0dc-8160-4f05-9de8-c9f1dad139c9" />

<img width="1384" height="599" alt="image" src="https://github.com/user-attachments/assets/b3c916c2-80f5-48bc-b742-f4582f7b6324" />

save and connect
--------------------------------
<img width="1030" height="248" alt="image" src="https://github.com/user-attachments/assets/9504b538-e3a2-4b14-b35d-68ef441650ca" />

Got an error
----------------------
<img width="1411" height="293" alt="image" src="https://github.com/user-attachments/assets/947786d7-0b53-4c43-aa0d-b8bc442cdbe9" />

side bar-> network access->under security tab-> ip address - allow from anywhere

-------------------------------------------
6. TRY CONNECTING THE MONGODB CLUSTER USING MONGODB COMPASS FROM PERSONAL LAPTOP
   --------------------------------------------------
   <img width="1492" height="775" alt="image" src="https://github.com/user-attachments/assets/abc101a5-3128-42a1-86c0-0e3b62258ef5" />

         Connected
   
         browse collections->create the database ->can give name to databse and collection
   
         imported data in the collection
   
         u can see the datas in ur mongodb cluster -> click browse collections
         


   <img width="1169" height="492" alt="image" src="https://github.com/user-attachments/assets/94cd26fc-2290-44b8-aaf2-ff2a693ed148" />

----------------------------------
can see the database collection called telecom data
-------------------------------------------------------
   <img width="1919" height="952" alt="image" src="https://github.com/user-attachments/assets/00018160-37ca-4117-95e3-027bac01b063" />

---------------------------------
uploaded the csv content there so we can see in the cluster
----------------------------------------------------------
<img width="1696" height="580" alt="image" src="https://github.com/user-attachments/assets/342f0f05-e204-4a58-804d-aaf2df1ba7fb" />

---------------------------------
7.connect to Grafana 
---------------------
8. Directly uploading data to grafana
   ---------------------------------------
     1. create dashboard
     2. select datasource as infinity
     3. select source as inline
     4. upload ur file
     5. visualization-> table
 <img width="1641" height="880" alt="image" src="https://github.com/user-attachments/assets/9a94b7c3-436e-48ac-93c5-97d1dc320449" />
  
-------------------
IMP: Grafana considers the column to be text most of the tym unless we set the transformation(convert field type -number)
---------------
 <img width="1620" height="849" alt="image" src="https://github.com/user-attachments/assets/6995039d-c8f3-4d56-be09-c4d4d241c568" />

-------------------------
value mappining -> 
----------------------
      can be done to give colour only to particular values

--------------------------------

Dashboard:
--------------------------
<img width="1614" height="838" alt="image" src="https://github.com/user-attachments/assets/ecf4e0a2-ccc7-4eb8-9851-cf8fcba707d5" />

-------------------------------
25/08/2025
-------------------------

1. Adding a panel togroup your data and calculate a total value for each group  using the summarize feature of infinity data source . 
   ----------------------------------------------------------------------------------------
            summarize field = type of calculation u want to perform -> sum(MonthlyCharge)
         
            Summarize By field, type the column you want to group your data by. For your bar chart, this should be PlanType.
            Parsing options & Result fields: add column ->PlanType ->string
            summarized result= column ->TotalMonthlyCharge and set its type to number
         
<img width="906" height="234" alt="image" src="https://github.com/user-attachments/assets/f03c316e-e874-4541-8bd2-9fb574683d62" />
<img width="751" height="257" alt="image" src="https://github.com/user-attachments/assets/602ef489-b9cf-472b-b533-495a85d84bab" />
<img width="766" height="224" alt="image" src="https://github.com/user-attachments/assets/65c010be-989b-43a0-8a95-5a23cd2c1b11" />

-------------------------------------------------------------------------------
2. What I have done here?
      -----------------------------------
         Group all your customers by their PlanType (e.g., grouping all "Prepaid" customers together).

         Calculate the sum of the MonthlyCharge for each of those groups.
------------------------------------------------
3. NewlyAdded panel:
   -----------------------------
   <img width="775" height="283" alt="image" src="https://github.com/user-attachments/assets/1d8cf81d-2fcb-4822-bc1b-641d9cb12a63" />
---------------------------
4. Sort the panel in increasing order
   -----------------------------------
   <img width="1254" height="178" alt="image" src="https://github.com/user-attachments/assets/ed900a13-727a-49cc-ae72-510e83315bb4" />
   <img width="1250" height="391" alt="image" src="https://github.com/user-attachments/assets/e7c08031-d654-4b4d-a6a8-88f06245872f" />


-------------------------
5. TOTAL CUSTOMERS:
   ------------------------------
   <img width="942" height="197" alt="image" src="https://github.com/user-attachments/assets/90d8908c-2093-4c98-ab48-ceee38cedc6d" />
   <img width="1085" height="165" alt="image" src="https://github.com/user-attachments/assets/89713a82-1f0d-43f2-a395-7da4b39f7aa0" />




   

         
         
   




