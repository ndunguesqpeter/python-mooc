num = int(input("Enter a number: "))
original = num
sum_digits = 0

while num > 0:
    last_digit = num % 10  #Get last digit
    sum_digits += last_digit
    num = num // 10

print(f"Last digit of {original} is {last_digit}")
print(f"Sum 0f digits = {sum_digits}")