1. create a channel in the teams

      <img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/be5acb42-e6ed-4a92-98a8-84c0094b3e41" />
-------------------------------------------------------------------------------------
2. ur channel name ->3 dots -> manage channels-> edit connectors ->search incoming webhook ->add
   
    <img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/be4395c8-88fd-430e-9ea8-c8e6afc0a00a" />
   
    <img width="1504" height="983" alt="image" src="https://github.com/user-attachments/assets/82ed5d60-90aa-4673-8533-fc6b37a45790" />

--------------------------------------------------------------------------------------------
3. copy the link
------------------------------------------------------------------------------------
4.  paste ur url in grafana cloud ->contact point ->microsoft teams

   <img width="1650" height="837" alt="image" src="https://github.com/user-attachments/assets/292cf7b7-a686-48f8-bc30-e0daa5151eef" />
      
 <img width="1600" height="714" alt="image" src="https://github.com/user-attachments/assets/98883143-0bc1-47f6-82a6-5e1eeb1f7a71" />

------------------------------------------------------------------------------
5. create alert rule

 <img width="1577" height="769" alt="image" src="https://github.com/user-attachments/assets/217b09fa-c71e-40ca-b827-52bd2ea68105" />

imp: In the query session give the same values in the panel(edit panel -> check min and max values and give)

<img width="1336" height="871" alt="image" src="https://github.com/user-attachments/assets/74db8068-1298-476a-b71c-ea55ed51bd74" />

            The condition says to notify alert if the error rate is above 5%.
            added folders and also labels

 labels:  type and enter

      <img width="849" height="552" alt="image" src="https://github.com/user-attachments/assets/2fa47eb1-76a8-4faa-8af5-ae0e0e7a3d73" />

Folders: To make the alerts organized...eg: production alerts,development alerts...all alerts belonged to that category grouped into that folder for quick look and understanding.

labels: quickly find the alerts based on the labels. (easy for searching and filtering the alerts)

evaluation behaviour: grafana will check alerts for every x mins and if it met any alert it will move to pending period .Grafana again checks the alert..is it true..and it last for Y mins..it will be sent to firing period and notification alert sents. Until the problem goes away it will be firing when its in firing state.



configuring contact points:

<img width="1296" height="855" alt="image" src="https://github.com/user-attachments/assets/6a710a14-9c6c-4ec9-80ef-4d0c8abeb361" />







   
