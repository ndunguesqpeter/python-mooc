# Get the upper limit from the user and convert it to an integer
upper_limit = int(input("Upper limit: "))

# Initialize a variable to store the sum of numbers
sum_of_numbers = 0
# Initialize a counter variable to keep track of the current number
number = 0

# Continue adding numbers to the sum until it exceeds or equals the upper limit
while sum_of_numbers < upper_limit:
    # Add the current number to the sum
    sum_of_numbers += number
    # Increment the current number
    number += 1

# Print the sum of numbers (which may have exceeded the upper limit in the last iteration)
print(sum_of_numbers)
"""
What the program is doing:
It asks the user to enter an upper limit, which is stored in the upper_limit variable.
It then enters a loop where it continuously adds consecutive integers (0, 1, 2, ...) to sum_of_numbers until sum_of_numbers is 
no longer less than upper_limit.
Once the loop condition is no longer met, it prints the final value of sum_of_numbers.
In essence, the program is calculating the sum of consecutive integers starting from 0 until the sum exceeds 
or equals the user-provided upper limit.

For example, if the user enters 2, the program will calculate the sum as follows:

sum_of_numbers = 0 + 0 = 0 (number = 1)
sum_of_numbers = 0 + 1 = 1 (number = 2)
sum_of_numbers = 1 + 2 = 3 (number = 3)
Since 3 is greater than 2, the loop exits, and 3 is printed as the result.
"""