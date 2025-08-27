Modifying Dashboard
------------------------------------
 Current Dashboard:
    
<img width="1660" height="770" alt="image" src="https://github.com/user-attachments/assets/c4156fb2-2cd1-4796-ac38-0e4cbf6c916a" />

Target Dashboard:
    
<img width="847" height="349" alt="image" src="https://github.com/user-attachments/assets/f8f0b245-0936-4402-b7e3-c1fb1d70ff0d" />


--------------------------
STEPS
------------------------------
1.  created the  1st panel using :

       <div style="color: black; background-color: pink; padding: 10px; text-align: center;">
      <h1>App Services Panels – Order Management, Product Config and Account Management</h1>
      </div>

      visualization: text

2.  then created panels for order management and account management and product config:
   
 csv data for order management:

timestamp,service,total_requests,success_pct,client_error_pct,server_error_pct,p99_s,available_services,unavailable_services,service_availability
2023-10-27T10:00:00Z,Order Management,5798,0.83,0,98.12,1.68,24,0,100
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100
2023-10-27T10:00:00Z,Product Config,0,0,0,0,0,30,0,100

csv data for account management:

timestamp,service,total_requests,success_pct,client_error_pct,server_error_pct,p99_s,available_services,unavailable_services,service_availability
2023-10-27T10:00:00Z,Order Management,5798,0.83,0,98.12,1.68,24,0,100
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100
2023-10-27T10:00:00Z,Product Config,0,0,0,0,0,30,0,100

csv data for product config:

timestamp,service,total_requests,success_pct,client_error_pct,server_error_pct,p99_s,available_services,unavailable_services,service_availability
2023-10-27T10:00:00Z,Order Management,5798,0.83,0,98.12,1.68,24,0,100
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100
2023-10-27T10:00:00Z,Product Config,0,0,0,0,0,30,0,100


csv data for calculating sum of the panels in the top:

timestamp,service,total_requests,success_pct,client_error_pct,server_error_pct,p99_s,available_services,unavailable_services,service_availability
2023-10-27T10:00:00Z,All,10946,46.42,1.05,52.5,1.68,84,0,100
2023-10-27T10:00:00Z,Order Management,5798,0.83,1.05,98.12,1.68,24,0,100
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100
2023-10-27T10:00:00Z,Product Config,0,0,0,0,0,30,0,100

------------------------------
DRILL DOWN METHOD
-------------------------

1. created a new dashboard:

    added a csv data:

timestamp,service,total_requests,success_pct,client_error_pct,server_error_pct,p99_s,available_services,unavailable_services,service_availability,status_code,error_message
2023-10-27T10:00:00Z,Order Management,5798,0.83,1.05,98.12,1.68,24,0,100,404,Not Found
2023-10-27T10:00:00Z,Order Management,5798,0.83,1.05,98.12,1.68,24,0,100,401,Unauthorized
2023-10-27T10:00:00Z,Order Management,5798,0.83,1.05,98.12,1.68,24,0,100,503,Service Unavailable
2023-10-27T10:00:00Z,Order Management,5798,0.83,1.05,98.12,1.68,24,0,100,500,Internal Server Error
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100,400,Bad Request
2023-10-27T10:00:00Z,Account Management,5140,97.92,2.08,0,0.85,30,0,100,403,Forbidden
2023-10-27T10:00:00Z,Product Config,0,0,0,0,0,30,0,100,200,OK

added variables:
 <img width="964" height="379" alt="image" src="https://github.com/user-attachments/assets/9d6123c7-d212-42fb-924b-55f61d54795c" />

 <img width="1024" height="352" alt="image" src="https://github.com/user-attachments/assets/7333b327-266d-4a54-900a-e627c7f0dcd0" />

 -------------------
 copy the number cbc5....
 -----------------------
 <img width="751" height="38" alt="image" src="https://github.com/user-attachments/assets/2c4e89cc-ab46-4719-8a88-27be43ad1ab7" />

url:  d/cbc5mhv/error-details?var-service= Account Management&var-error_class=4xx

     give this url for each datalink...change the service namees for each panel..
     edit the client error panel.. add data link.. paste the url.. change the account management into product config..if doing with that panel..

  -------------------------
  OUTPUT
  ----------------------------
  when u click the client error panel it will redirect to the other dashboard ...about the errors
  <img width="1384" height="393" alt="image" src="https://github.com/user-attachments/assets/b3eec915-d9e5-4348-af8b-149e9b0edefe" />
  <img width="1509" height="298" alt="image" src="https://github.com/user-attachments/assets/ae2fcf00-7882-4641-b622-f4349cede6bf" />
  <img width="1553" height="326" alt="image" src="https://github.com/user-attachments/assets/249ff475-9078-42bd-a664-a9039186a226" />



 


