#single  level inheritance
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A): #inherited class
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(B): #inherited class from B (Multilevel Inheritance)
    def feature5(self):
        print("feature 5 is working")

a1=A()
b1=B()
c1= C()

a1.feature1()
a1.feature2()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

#can access all methods
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

# superclass = class A(parent class)
# subclass = Class B (Child class) inherited class from a parent class

# multilevel inheritance: A child class can access all the behaviours from parent class,
#                        grand parent class and its ancestors
