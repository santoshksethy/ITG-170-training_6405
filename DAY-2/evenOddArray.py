#even and odd numbers in an array
arr = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even numbers:")

for i in arr:
    if i % 2 == 0:
        print(i,end=" ")
print()
print("Odd numbers:")

for i in arr:
    if i % 2 != 0:
        print(i)