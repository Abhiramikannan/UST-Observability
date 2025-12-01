#https://www.youtube.com/watch?v=sioSarg0-nU&list=PLsyeobzWxl7omDoEYrrf3oXvXxa6MPgek&index=17

# #swapping 2 variables in python
a=5
b=6

#write the normal logic here and change(a=b,b=a  then add a variable c and store the value of a into it and change b in 3rd step)
c=a
a=b
b=c  #changed to c

print("a :", a)
print("b: ",b)



#avoid 3rd variable and use mathematical formula
#saving memory
a=5
b=6
a=a+b # a=5+6=11
b=a-b # b=11-6=5
a= a-b # a=11-5=6
print("a :", a)
print("b: ",b)


#again to avoid losing extra bits we can use xor(^)
a=5
b=6
a=a^b 
b=a^b 
a= a^b 
print("a :", a)
print("b: ",b)

#easiest way
a=5
b=6
a,b=b,a  # tuple packing is happening when we fetch the data 5 and 6 and tuple unpacking is happening when we swap it..
print("a :", a)
print("b: ",b)
