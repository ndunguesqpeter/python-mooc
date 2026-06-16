num = int(input("Enter a number: "))
original = num
digit_count = 0
last_two = num % 100  #Get last 2 digits

while num > 0:
    digit_count += 1
    num = num // 10
    
print(f"Total digits: {digit_count}")
print(f"Last two digits: {last_two:02d}")