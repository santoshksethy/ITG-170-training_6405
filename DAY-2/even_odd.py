def q19():
    n = input("Enter a number: ")
    even_sum = sum(int(d) for d in n if int(d) % 2 == 0)
    odd_sum  = sum(int(d) for d in n if int(d) % 2 != 0)
    print(f"Sum of even digits = {even_sum}")
    print(f"Sum of odd digits  = {odd_sum}")