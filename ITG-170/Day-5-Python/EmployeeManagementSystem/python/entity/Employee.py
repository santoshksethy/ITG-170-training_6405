class Employee:
    def __init__(self,id=100,name='default',role='default',age=18,salary=15000):
        self.id = id
        self.name = name
        self.role = role
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'{self.name} is working as {self.role} with age of {self.age} holding id-number of {self.id}'
