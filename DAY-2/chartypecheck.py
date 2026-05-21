char=input("Enter a character: ")
if char.isupper():
    print(f"{char} is an uppercase letter.")
elif char.islower():
    print(f"{char} is a lowercase letter.")
elif char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is a special character.")