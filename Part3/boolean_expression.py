#Any boolean expression or combination thereof is a valid condition in a loop
#initialise
number = int(input("Number: "))
#Condition
while number < 100 and number%5 != 0:
    print(number)
    number += 3
#Update variables