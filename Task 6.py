# Task 6: Polymorphism and Overriding
class Animal:
    def sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.sound()

# Demonstration of Task 6
dog = Dog()
cat = Cat()
make_animal_sound(dog)
make_animal_sound(cat)