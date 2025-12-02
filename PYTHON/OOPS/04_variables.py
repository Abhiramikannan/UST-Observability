# 2 types of variables
#     instance variables
#     static variables

#instance variables: As the object changes this value also change.
    #variable created inside init will become instance variable

class Car:
    
    wheels=4 #static variable/class variable = which is common to all objects created

    def __init__(self):
        self.mil=10 #instance variable
        self.com="BMW" #instance variable
        


c1=Car()
c1.com="ambasder" #value changed.
c2=Car()
print(c1.com,c1.mil,c1.wheels) #wheels also added
print(c2.com,c2.mil,c2.wheels)


#static variable
    #variable created inside init
    #define a variable outside init and inside the class called class variable
 
#  Namespace?
# 	its an area where u create  and store object/variable.
# 	class namespace = class variables
# 	instance namespace=instance variables
