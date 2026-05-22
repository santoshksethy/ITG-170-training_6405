try:
    num1 = int(input("Enter first number: "))

    try:
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print(e)