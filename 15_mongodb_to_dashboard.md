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

side bar-> network access->under security tab-> 




