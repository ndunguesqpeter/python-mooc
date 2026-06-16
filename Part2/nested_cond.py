#Nested conditions i.e condition within a condition
#input
num  = int(input("Please enter a number: "))
if num > 0:
    if num%2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
else:
    print("The number is zero")
