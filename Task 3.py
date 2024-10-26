#Multilevel inheritance
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        print(f"The{self.vehicle_type} is starting.")
    
    class Car(Vehicle):
        def __init__(self, vehicle_type, number_of_doors):
            super().__init__(vehicle_type)
            self.number_of_doors = number_of_doors

class electric_car(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity

#demonstration
electriccar = electric_car('Tesla', 4,'120 kwh')
electric_car.start()

print (f'number of doors: {electric_car.number_of_doors}')
print (f'battery capacity: {electric_car.battery_capacity}')