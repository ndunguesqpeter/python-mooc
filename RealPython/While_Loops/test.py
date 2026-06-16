num = int(input("Please enter a number: "))

while num > 0:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    num -= 1