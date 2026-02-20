LAMBDA FUNCTION
------------------------
1. Essential to perform the API calls like describeHosts and describeInstances and sent those data to cloudwatch and also to publish custom metrics.
2. Steps to create lambda function
<img width="1754" height="686" alt="image" src="https://github.com/user-attachments/assets/2e4f9064-c045-4ce8-9856-2b779816dfba" />
<img width="1748" height="589" alt="image" src="https://github.com/user-attachments/assets/8281129f-9b29-4350-adc5-4de588a228a3" />
<img width="1342" height="769" alt="image" src="https://github.com/user-attachments/assets/f197e3a7-d8f3-4318-944f-a2cb03f781f0" />
<img width="1425" height="779" alt="image" src="https://github.com/user-attachments/assets/131ab7c8-3e20-49ea-95b2-2f5733ed827c" />


Error:
----------------------
1. I got this error while enabling the vpc and without enabling vpc also.
2. Varun said to me : the lambda must be created within the shared lambda vpc. Also to verify the NAT gateway is available for the shared Lambda VPC.
3. But there was no NAT gateway created.
4. I raised a CSRE ticket for the NAT gateway and lambda creation Issues.
   


