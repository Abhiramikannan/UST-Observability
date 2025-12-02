#constructor,self, and comparing objects in python

class Computer:
    pass

c1=Computer() #created object , object taken some spaces on heap memory
print(id(c1)) #To get the address



#NOTES
#in our computer we will be having heap memory.. which contains all the objects(int,string)
#object will take some space in your heap memory
#every space will have an address


#id() function = to get address

#What happens if i create another object?
c2=Computer()
print(id(c2))  #diffrent address space

#whenever u create object it will take diff address space

#how much size it will take and who will allocate the memory to object?
    #size of an object depends upon
        #no: of variables
        #size of each varibale
    # who allocates size to object
        #constructor...call init method for you internally.



#compare 2 ages

class Computer:
    def __init__(self):
        self.name="navin"
        self.age=20
    def update(self):
        self.age=30

    #comparing
    def compare(self,other): #c1 will become self and c2 will become other
        if self.age==other.age:
            return True
        else:
            return False
        

c1=Computer()
c2=Computer()


c1.name="rashi"
c1.age=12

if c1.compare(c2):
    print("They are same")
else:
    print("different")



print(c1.name)
print(c2.name)


#compare():
	#takes 2 parameters: who is calling, whom to compare.
