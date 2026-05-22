# 1. Manually writing the custom exception class
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        # Use super() to pass the message to the base Exception class
        super().__init__(self.message)

# 2. Logic that uses the 'raise' keyword
def check_employee_eligibility(salary):
    if not (5000 < salary < 15000):
        # Triggering the custom exception manually
        raise SalaryNotInRangeError(salary)
    
    print(f"Success! Salary of ${salary} is approved for this role.")

# 3. Execution and handling
if __name__ == "__main__":
    #test_salaries = [8000, 2000]
    amount=int(input("Enter the salary:"))
    #
    try:
        print(f"Checking salary: ${amount}...")
        check_employee_eligibility(amount)
    except SalaryNotInRangeError as e:
        # Accessing the custom attributes we defined manually
        print(f"Caught an Exception: {e.message}")
        print(f"Invalid Input: {e.salary}")
        print("-" * 20)