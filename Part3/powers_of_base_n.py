# Get the upper limit from the user and convert it to an integer
upper_limit = int(input("Upper limit: "))

# Get the base from the user and convert it to an integer
base = int(input("Base: "))

# Initialize the number to start with (1 is a common starting point for powers)
number = 1

# Continue looping as long as the current number is less than or equal to the upper limit
while number <= upper_limit:
    # Print the current number
    print(number)
    # Multiply the current number by the base to get the next number in the sequence
    number *= base