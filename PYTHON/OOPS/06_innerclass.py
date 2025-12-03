# innerclass: class inside a class can be created
# for example : create a student class with name ,roll no etc.. he have laptop, that details can be created
# in a different class in the same class.
#     adv: provide a clean namespace 

class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        self.lap=self.Laptop() #created object for inner class
    
    def show(self):
        print(self.name,self.rollnumber)
        self.lap.show() #calling innerclass
    
    class Laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("abhi",4)
s2=Student("selmi",6)

#calling the methods
s1.show() #prints outer class


#can create object of inner class inside the outer class
