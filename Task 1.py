#Task 1: Single inheritance
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
class smartphone(Device):
    def __init__(self, brand, model,storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity
    def show_info(self):
        super().show_info() #call the parent method
        print(f"Storage Capacity: {self.storage_capacity} GB")

#Demostration of task 1
smartphone1 = smartphone("Apple", "iPhone 13", 128)
smartphone2= smartphone('Samsung','Samsung S24',256)
smartphone1.show_info()
smartphone2.show_info()