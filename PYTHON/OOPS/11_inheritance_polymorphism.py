class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
    def move(self):
        print("vehicle moves")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("plane flies")

v1=Vehicle("tata","black")
c1=Car("abc","white")
p1=Plane("xyz","green")

for x in v1,c1,p1:
    print(x.brand)
    print(x.colour)
    x.move()
    

