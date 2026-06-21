# Ask the user for an upper limit and convert their input to an integer
upper_limit = int(input("Upper limit: "))

# Initialize a variable to 1, which is the first power of 2
number = 1

# Continue the loop as long as the current number is less than or equal to the upper limit
while number <= upper_limit:
    # Print the current number
    print(number)
    # Double the current number for the next iteration
    number *= 2