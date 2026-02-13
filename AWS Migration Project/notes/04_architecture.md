ARCHITECTURE
-----------------------------
<img width="944" height="651" alt="image" src="https://github.com/user-attachments/assets/1b60f50c-3d75-4aac-985d-74fb170b322b" />

CLEAR VIEW
---------------------
<img width="1669" height="414" alt="image" src="https://github.com/user-attachments/assets/352b6ef4-526e-4943-8064-a130b2c2f722" />
<img width="1575" height="693" alt="image" src="https://github.com/user-attachments/assets/1936d736-7bf8-4e38-a78b-8ee99ff6a26d" />

Eventbridge Rule
-------------------------
1. Target will be lambda
2. 15 mins lambda triggering using crone like schedule: the utilization of host will change and it is not related to events so to cover that we need polling, for polling the lambda will call only DescribeHosts api
