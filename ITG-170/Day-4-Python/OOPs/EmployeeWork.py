class Employee:
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print('Employee is working')
    def getSalary(self):
        return self.salary

e= Employee(34000)
e.work()
print(e.getSalary())