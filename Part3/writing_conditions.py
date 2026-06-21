# Print Numbers program: prints a sequence of numbers starting from user input
# until the number reaches 100 or becomes divisible by 5.

# Get user input and convert it to an integer
number = int(input("Number: "))

# Continue printing and incrementing the number while it is less than 100
# and not divisible by 5
while number < 100 and number % 5 != 0:
    # Print the current number
    print(number)
    # Increment the number by 3 for the next iteration
    number += 3