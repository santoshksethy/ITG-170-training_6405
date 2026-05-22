arr = [1, 2, 2, 3, 4, 1, 2, 5]

visited = []

for element in arr:
    if element not in visited:
        count = arr.count(element)
        print(f"{element} occurs {count} times")
        visited.append(element)