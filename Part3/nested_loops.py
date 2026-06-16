# Ask the user for a number (currently hardcoded to 5 for testing)
number = 5  # int(input("Please enter a number:"))

# Continue looping until the number becomes 0 or less
while number > 0:
    # Initialize a counter variable to 0 for the inner loop
    i = 0
    
    # Print numbers from 0 up to but not including the current number
    while i < number:
        # Print the current value of i followed by a space, without starting a new line
        print(f"{i} ", end="")
        # Increment i by 1 for the next iteration
        i += 1
    
    # Start a new line after printing the numbers for the current iteration
    print()
    
    # Decrement the number by 1 for the next iteration of the outer loop
    number -= 1