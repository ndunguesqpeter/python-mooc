#Progam tha prints out all 11 numbers (2-30) using a loop
#initialise
num = int(input("Please enter a number: "))
#Condition
while 2 <= num < 30:
    if num%2 == 0:
        print(num)
#Update variables
    num += 1
