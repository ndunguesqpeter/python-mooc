number = int(input("Please enter a number: "))
value1 = 1
while value1 <= number:
    value2 = 1
    while value2 <= number:
        print(f"{value1} * {value2} = {value1 * value2}")
        value2 += 1
    print()
    value1 += 1