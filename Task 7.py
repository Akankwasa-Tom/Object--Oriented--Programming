# Task 7: Multiple Inheritance with super()
class DeviceInfo:
    def info(self):
        print("Device information.")

class Computer(DeviceInfo):
    def info(self):
        print("Computer information.")

class Laptop(Computer):
    def info(self):
        super().info()  # Call Computer's info
        print("Laptop information.")

# Demonstration 
laptop = Laptop()
laptop.info()