class A:

    def __init__(self):
        print("class A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A): 
    def __init__(self):
        super().__init__() #try to call init method  of class A
        print("class B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")


#a1=A() #which calls method which is __init__
a1=B() #it calls constructor of A if we didnt  create object for A even.
#what if u have your own init method? what if class B also have init?
    #prints class B 's init 


#if u create object of subclass, first it will try to find init of subclass if not there, then it find init of super class.
#when u create object of subclass it will call init of subclass first , if u have call super then it will
#call init of super class then call init of sub class

class C(A,B):
    def __init__(self):
        print("class c init")


c1=C()

#Method Resolution Order (MRO)= left to right...
#super().__init__() =in class C(A,B) ..choose A s init method first
