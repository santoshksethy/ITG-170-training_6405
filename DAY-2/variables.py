list_a = [10, 20]
list_b = [10, 20]
list_c = list_a


print("Do A and B have the same values?")
print(list_a == list_b)

print("Are A and B the exact same object in memory?")
print(list_a is list_b)

print("Are A and C the exact same object in memory?")
print(list_a is list_c)