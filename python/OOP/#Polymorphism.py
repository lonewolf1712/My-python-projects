#Polymorphism
class Stuti:
    def speak (self):
        print("Stuti is moaning.")
class Daksh:
    def speak (self):
        print("Daksh is growling.")
def make_sound(speaker):
    speaker.speak()
make_sound(Stuti())
make_sound(Daksh())
