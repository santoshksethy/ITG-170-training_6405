#Program to Print Armstrong Number between 1 to 1000.
# Find Armstrong numbers from 1 to 1000

for num in range(1, 1001):

    num_str = str(num)
    n = len(num_str)

    sum_of_powers = 0
    temp = num

    # Calculate sum of digits raised to the power of n
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10

    # Check Armstrong number
    if num == sum_of_powers:
        print(num)
