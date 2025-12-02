#__init__method in python
# 1. what objects have?
# 	attributes
# 	behaviour

# 2. what class have?
# 	methods,properties


# 3. example:
# 	car 
# 	attributes: colour,model,speed
# 	behaviour: start,stop,accelerate
# 	methods: functions
# 	properties: special way to access attributes 

#__INIT__: To initialize the variable
#if we didnt call it also it got executed (Depends upon how many objects we created and used.
#eg:
class computer:
    def __init__(self):
        print("init got printed") #twicely printed because u called 2 objects 
    def config(self):
        print("i7,16GB,1TB")

comp1=computer() 
comp2=computer()

#calling the method using comp1 object
computer.config(comp1)
computer.config(comp2)

#output:
# init got printed
# init got printed
# i7,16GB,1TB
# i7,16GB,1TB




#when we call a function actually we are passing object itself as a parameter automatically if nothing in bracket also.
class computer:
    def __init__(self,cpu,ram): #passed 2 parameters
        self.cpu=cpu  #accept cpu as i5 in object 1
        self.ram=ram #accept cpu as ryzen3 in object2 

        
    def config(self):
        print("config is", self.cpu, self.ram)

comp1=computer("i5",16) # we are actually passing 3 arguments.. object,i5,16
comp2=computer("RYzen 3",8) #3 arguments

comp1.config()
comp2.config()


#example2
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def Employee_details(self):
        print(self.name,self.age,self.salary)


   
emp1=Employee("harsha",38,6000)
emp2=Employee("anu",22,30000)

emp1.Employee_details()
emp2.Employee_details()

