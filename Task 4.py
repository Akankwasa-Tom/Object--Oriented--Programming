# Task 4: Method Overriding
class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

class Developer(Employee):
    def work(self):
        print("Developer is writing code.")

# Demonstration of Task 4
manager = Manager()
developer = Developer()
manager.work()
developer.work()