#To solve any problem in real life we see everything as objects.
#human, camera , ...everything is object in virtual world.
#employee is an object and employee id, name, salary all its parameters. Behaviour of employees are they talk, drink coffee...



# if u want object.. first create class which is blueprint.
#in oops the functions are called as methods.
#class will have properties and methods


a=10
print(type(a)) ##object of type class int

class computer:
    pass
comp1=computer() #() is imp
print(type(comp1)) # class of type computer





# when u create a function inside a class = it will become method
class computer:
    def config(self): #self is used in python.. self is the object that we are passing while calling the method.
        print("i7,16GB,1TB")

comp1=computer() #created object for class computer
comp2=computer()#created 2nd object comp2

#calling the method using comp1 object
computer.config(comp1)
computer.config(comp2) #these objects will pass on self

#self is used to get current object that we are using
#1 class will contain multiple objects
#To take the object we are calling here we define self and passing the object in () ...computer.config(comp1)


#this also works
comp1.config() # comp1 is passed as an parameter now
comp2.config()




