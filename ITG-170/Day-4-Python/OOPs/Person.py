class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def getFirstName(self):
        return self.first
    def getLastName(self):
        return self.last

p = Person('john','jacob')
print(p.getFirstName())
print(p.getLastName())