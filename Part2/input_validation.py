# Import the sqrt function from the math module to calculate square roots
from math import sqrt

# Create an infinite loop that continues until a certain condition is met
while True:
    # Prompt the user to enter a number and convert the input to an integer
    number = int(input("Please type in a number: "))
    
    # Check if the input number is 0, and if so, exit the loop
    if number == 0:
        break
    
    # Check if the input number is positive
    if number > 0:
        # Calculate the square root of the number using the sqrt function
        square_root = sqrt(number)
        # Print the calculated square root
        print(square_root)
    else:
        # If the number is not positive, print an error message
        print("Invalid number.")

# Print a message indicating that the program is exiting
print("Exiting...")