count = 0
sum = 0
while True:
    number = int(input("Please type in integer number. [Type in 0 to finish.] Number: "))
    
    if number == 0:
        break
    count += 1
    sum += number
    mean = sum/count
    
print(f"The entries of the numbers are {count}.")
print(f"The sum of the numbers is {sum}")
print(f"The mean is {mean}.")