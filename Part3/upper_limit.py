# Get the upper limit from the user and convert it to an integer
number = int(input("Upper limit:"))

# Initialize a variable to keep track of the current number to print
upper = 1

# Continue printing numbers until we reach the user-specified upper limit
while upper < number:
    # Print the current number
    print(upper)
    # Increment the current number by 1
    upper += 1

# Print a message to indicate the end of the output
print("End")