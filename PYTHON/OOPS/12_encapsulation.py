#encapsulation is keeping the methods and the data together in a class while protecting the data accessed
#from outside the class

#To make properties private use double underscore __
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #private
    def get_age(self): #getter method to access private properties
        return self.__age
    def set_age(self,age):#setter method to set the value of private properties
        if age > 0:
            self.__age=age 
        else:
            print("age must be +ve")



p1=Person("abhi",23)
print(p1.name)
print(p1.get_age()) #will get age
#print(p1.__age)  # returns error
#private properties cannot be accessed outside the class


#to access =create getter method
#setters
p1.set_age(34)
print(p1.get_age())
    
