#https://www.youtube.com/watch?v=Ye3vV4QQ_js&list=PLsyeobzWxl7omDoEYrrf3oXvXxa6MPgek&index=18
taking input from keyboard
a=input()
b=input()
a,b=b,a  
print("a :", a)
print("b: ",b)

#to more clear u can add enter the number
a=input("enter the 1st num")
b=input("enter the 2nd num")
a,b=b,a  
print("a :", a)
print("b: ",b)

#input() is a function which takes something from u and returns string
a=input("enter the 1st num") #3
b=input("enter the 2nd num") #5
c=a+b #35
print(c)  #expected output 8

#so use int(input())
a=int(input("enter the 1st num")) #3
b=int(input("enter the 2nd num")) #5
c=a+b #35
print(c)  #expected output 8


#if u want to print a charecter
a=input("enter the charecter ") #you
print(a) 
print(a[0]) #to access the first letter

#to save memory
a=input("enter the charecter "),a[0]  #use a[0] here
print(a)


