#numpy: Numerical python


import numpy as np
arr=np.array([1,2,3,4,5]) #converting this list[1,2,3,4,5] to array
print(arr)
print(type(arr))

#version checking
print(np.__version__)

#tuple to array
arr=np.array((1,2,3,4,5))
print(arr)

#0 Dimension Array
arr=np.array((42))
print(arr)

#1 D array
arr0=np.array([1,2,3,3])
print(arr0)

#2 D array
arr=np.array([[1,2,3],[3,4,4]])
print(arr)

#3 D array
arr1=np.array([
    [[1,2,3],[4,5,6]], #depth 0 # 2 row, 3 column
    [[1,2,3],[4,5,6]] #depth 1
    ])
print("3d array is \n",arr1)

#how many dimension an array have? #ndim attribute
print("arrays dimension is:",arr1.ndim)

#access 1 D array elements
print(arr0[0])
print(arr0[1]) # 2nd element

#access 2 D array element
arr2=np.array([[1,2,3],[3,4,5]])
print("the 2nd element of 1st row is: ",arr2[0,1])

#access 3 D array element:
arr1=np.array([
    [[1,2,3],[4,5,6]], #depth 0 # 2 row, 3 column
    [[7,6,0],[1,9,2]] #depth 1
    ])

print(arr1[0,1,2]) # 0 depth,1 =row1,2=column2
#arr1[0]=[1,2,3],[4,5,6]
#arr1[0,1]= 2nd row [4,5,6]
#arr1[0,1,2]=3rd column that is [6]

#negative slicing
arr4=np.array([1,2,3,4,5])
print(arr4[-3:-1])  #arr1[-3:-1] means: start at index -3 (value 3), go up to but not including index -1 (value 5).
#So it returns: [3, 4].

#step value to determine the step of the slicing
print(arr4[1:5:2]) #from index 1 to index 5(not included) skip 1

#slicing 2 d arrays
arr5=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr5[1,1:4]) # 1st row il index 1 to 4

#dtype = returns the data type of the array
print(arr4.dtype)


#creating array with defined datatype
arr6=np.array([1,2,3],dtype='S')
print(arr6)
print(arr6.dtype)


arr6=np.array([1,2,3],dtype='i4')
print(arr6)
print(arr6.dtype)


#convert float to integer using 'i' as parameter value
# astype():
#     creates copy of array

arr7=np.array([1.0,2.0,34.3,5.1,8.9])
newarr=arr7.astype('i')
print(newarr)
print(newarr.dtype)

#float to int
newarr1=arr7.astype(int)
print(newarr1)
print(newarr1.dtype)

#copy and view
arr8=np.array([1,2,3,4,5])
arrcopy=arr8.copy()
arr8[1]=60
print(arr8) #  chaged array
print(arrcopy) #copied array
x=arr8.view()
print(x)


#if array owns its own data  =return none /not? =refer original object
arr9=np.array([1,2,3,4,5,6])
x=arr9.copy()
y=arr9.view()

print(x.base) #array have its own data
print(y.base) #refer the arrays memory


#shape() 2 D array: shows how many elements in each dimension
arr3=np.array([[1,2,3],[5,6,7]])
print(arr3.shape)
# It has:
# 2 rows
# 3 columns
# So arr3.shape returns a tuple (2, 3).



#reshape = add/remove/change no of elements in each dimension
arr7=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped_arr=arr7.reshape(4,3)
print(reshaped_arr)



#Vectorized operations
ms = np.array([95, 88, 102, 110, 98])   # CPU usage metrics

high_cpu = ms + 5          # add 5 to every metric
over_100 = ms > 100        # boolean array
print(ms[over_100])        # filter — values above 100

