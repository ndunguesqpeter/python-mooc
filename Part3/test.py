upper_limit = int(input("Upper limit: "))
sum_of_numbers = 1
number = 1
next_number = "1"

while sum_of_numbers < upper_limit:
    number += 1
    sum_of_numbers += number
    next_number += f" + {number}"
print(f"The consucutive sum : {next_number} = {sum_of_numbers}")