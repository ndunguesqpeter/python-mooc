numbers = 0
attempts = 0
positive = 0
negative = 0
equation = "0"

while True:
    number = int(input("Number:"))
    
    if number == 0:
        break
    attempts += 1
    numbers += number
    equation += " + " + str(number)
    if number > 0:
        positive += 1
    negative += 1  
print(f"...the program asks for Numbers typed in {attempts}")
print(f"The sum  :{equation} numbers is {numbers}")
print(f"The mean of the numbers is {numbers/attempts}")
print(f"Positive numbers{positive}")
print(f"negative numbers{negative}")