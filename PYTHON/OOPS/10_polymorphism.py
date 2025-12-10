#same method on diff class
class Car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
    def move(self):
        print("car moves")

class Ship:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("ship sail")

c1= Car("Ford","black")
s1=Ship("HAKKIN","white")

for x in c1,s1:
    x.move()


#same method in diff class but they print different.
