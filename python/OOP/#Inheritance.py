#Inheritance
class Car:
    def seats(self):
        print("5 seater")
class Electric_car(Car):
    def battery_size(self):
        print("2 meter")
sedan= Electric_car()
sedan.seats()
sedan.battery_size()