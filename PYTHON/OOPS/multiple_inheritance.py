class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B: 
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

#C says i want to access features from both A and B
class C(A,B): #  C can access both the classes.
    def feature5(self):
        print("feature 5 is working")

a1=A()
b1=B()
c1=C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

#A and B 2 diff classes and C can access everything from A and B
