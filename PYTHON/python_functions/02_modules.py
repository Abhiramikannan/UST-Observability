#https://www.youtube.com/watch?v=vPLaFFNGe7A&list=PLsyeobzWxl7omDoEYrrf3oXvXxa6MPgek&index=16

#module in python is like we can use in any programs.. which contains lots of functions.
#if u want to find square root of a number you can use sqrt() function by importing math module
#module contains many buildin functions,variables .. that can be used in program any time by importing it.
import math
num=25
b=math.sqrt(num)
print(b)

#directly can import using below line and dont want to use math.sqrt(num)
from math import sqrt # here imported so dont want to write math.sqrt(num)
num=25
b=sqrt(num) # no need of math here now
print(b)



#floor
  #will give you the lowest value

#ceil
  #ceil will give you highest value

#pow:
  #gives power value

#ceil,floor,pow
from math import sqrt,ceil,pow,floor
num=25
n=7.9
b=sqrt(num)
c=ceil(n) 
d=floor(n)
e=pow(2,3)  #gives 2 power 3
print(b)  #square root
print(c) #ceil
print(d) #floor
print(e) #power


#allias
import math as m #as m ..so it will be m 
a=m.sqrt(25)
print(a


      
