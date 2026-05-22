#static method
class Math:
        """Static method :method that does not change any istance of class
         here we created a static method to add two numbers"""
        @staticmethod
        def add(a,b):
            return a+b
result=Math.add(5,10)
print("Result:",result)