temperature = int(input("Enter the current temperature in degrees Celsius: "))
print("The current temperature is:", temperature)

is_pleasant = 20 < temperature < 30

print("Is the temperature between 20 and 30 degrees?")
print(is_pleasant)

if 20 < temperature < 30:
    print("The weather is perfect for a walk.")