#accessing private members using public member function
class Car:
    def __init__(self,name,model,year):
        """Private members are defined with double underscores and cannot be accessed directly from outside the class. 
        However, we can access them using public member functions (methods) that are defined within the class."""
        self.__name=name
        self._year=year
        self.model=model
    def printDetails(self):
        """Public member function to access private members"""
        print("Name:",self.__name)#private member
        print("Model:",self.model)#public member
        print("Year:",self._year)#protected member
class Bike(Car):
    """ In this example, we have a Car class with private members __name and _year.
      We also have a public member function printDetails() that accesses these private members.
        The Bike class inherits from Car and can call the printDetails() method to access the private members of the Car class."""
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
    def printDetails(self):
        """Overriding the printDetails method to access private members of the Car class"""
        print(f"Bike name:{self._Car__name}, Model:{self.model}, Year:{self._year}")
car1=Bike("BMW","X5",2020)
car1.printDetails()