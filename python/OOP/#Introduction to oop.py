#Introduction to oop
class Car:
    def __init__(self,brand,model,year):
        self.brand= brand
        self.model= model
        self.year= year
    def car_driving(self):
        print(f"Daksh is driving {self.brand} crazy")

car1= Car('Ford','sonet','2006')
car1.car_driving()