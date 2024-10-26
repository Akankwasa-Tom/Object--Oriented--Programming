# Multiple inheritance
class camera:   # parent class

    def take_photo(self):
        print("taking a photo")
class phone:  #  parent class

    def make_call(self):
        print("making a call")

class smartphone(camera,phone):   # child class
    pass
# Demonstration
smartphone = smartphone()
smartphone.take_photo()
smartphone.make_call()
