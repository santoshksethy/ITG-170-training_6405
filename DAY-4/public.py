#public access
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.age}")
e=Employee("kalyan", 30)
e.printDetails()