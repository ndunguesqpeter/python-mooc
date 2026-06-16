# Prompt the user to enter a number and store it in the 'number' variable
number = int(input("Please type in a number:"))
while True:
# Check if the input number is less than or equal to 0
    if number <= 0:
        # If true, print a goodbye message and exit the program
        print("Thanks and bye!")
        break
    else:
        # Initialize the 'factorial' variable to 1, which is the multiplicative identity
        factorial = 1
        # Initialize a counter variable 'i' to 1
        i = 1
        
        # Continue the loop as long as 'i' is less than or equal to 'number'
        while i <= number:
            # In each iteration, multiply 'factorial' by 'i'
            factorial *= i
            # Increment 'i' by 1 for the next iteration
            i += 1
        
        # Print the calculated factorial of 'number'
        print(f"The factorial of the number {number} is {factorial}")
        break