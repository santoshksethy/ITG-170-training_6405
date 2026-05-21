# Create a subclass called HRManager that overrides the work() method and
# adds a new method called addEmployee().
class Employee:
    def work(self):
        print("Employee is working.")

class HRManager(Employee):
    def work(self):
        print("HR Manager is working.")

    def addEmployee(self):
        print("Employee added.")
h1=HRManager()
h1.work()
h1.addEmployee()