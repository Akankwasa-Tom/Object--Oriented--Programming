# Task 5: Using super() Function
class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size

    def show_details(self):
        print(f"Brand: {self.brand}, Power: {self.power}W, Drum Size: {self.drum_size}kg")

# Demonstration of Task 5
washing_machine = WashingMachine("LG", 500, 7)
washing_machine.show_details()