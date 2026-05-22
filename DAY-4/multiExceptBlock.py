#multi except block
try:
    amount=int(input("ENter amount: "))
    atm_balance=1000
    if amount>atm_balance:
        raise ArithmeticError("Insufficient balance")
except ValueError:
    print("Invalid input. Please enter a valid amount.")
except ArithmeticError as e:
    print(e)
