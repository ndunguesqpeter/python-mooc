def remainder_calculator():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    
    if second_num == 0:
        print("Cannot divide by zero!")
    else:
        quotient = first_num // second_num
        remainder = first_num % second_num
        print(f"{first_num} / {second_num} = {quotient} with remainder of {remainder}")

remainder_calculator()