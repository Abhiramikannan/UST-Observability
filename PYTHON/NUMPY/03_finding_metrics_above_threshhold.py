#Detect metrics breaching thresholds
import numpy as np
arr1=np.array([1,2,3,4,5,80,120])
threshold=10
# alerts=arr1[arr1>threshold]
# print("alert values",alerts)
for value in arr1: #each value in arr1
    if value>threshold: 
        print("alert value is: ",value) #that value
   
