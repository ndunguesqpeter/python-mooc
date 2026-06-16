numbers = 0
attempts = 0

while True:
    number = int(input("Number:"))
    
    if number == 0:
        break
    attempts += 1
    numbers += number
print(numbers)