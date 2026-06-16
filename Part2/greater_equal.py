#Greater than or equal to
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in another number: "))
#condtion
if num1 > num2:
#print the result
    print(f"The greater number was:{num1}")
elif num2 > num1:
    print(f"The greater number was:{num2}")
else:
    print("The numbers are equal!")