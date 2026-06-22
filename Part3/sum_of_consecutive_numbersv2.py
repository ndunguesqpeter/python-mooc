# Get the upper limit from the user and convert it to an integer
upper_limit = int(input("Upper limit: "))

# Initialize variables to keep track of the sum and the numbers being added
sum_of_numbers = 1  # start with the sum of 1
number = 1  # current number being added
next_number = "1"  # string representation of the numbers being added

# Continue adding numbers until the sum exceeds the upper limit
while sum_of_numbers < upper_limit:
    # Increment the current number
    number += 1
    # Add the current number to the sum
    sum_of_numbers += number
    # Append the current number to the string representation
    next_number += f" + {number}"

# Print the final sum and the sequence of numbers that were added
print(f"The consecutive sum: {next_number} = {sum_of_numbers}")

"""
Program Behavior
The program is designed to calculate the sum of consecutive integers starting from 1 until 
the sum exceeds the user-provided upper_limit. Here's a step-by-step breakdown:

It initializes sum_of_numbers to 1, number to 1, and next_number to "1".
The while loop increments number by 1, adds it to sum_of_numbers, and appends it to next_number in each iteration.
The loop continues until sum_of_numbers is no longer less than upper_limit.
Finally, it prints the consecutive sum, the numbers that make up the sum, and the final sum.
For example, if the user enters "2", the output will be
"""