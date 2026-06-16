# Get user input and convert it to an integer
number = int(input("Please type in a number:"))

# Initialize the outer loop counter
i = 1

# Outer loop: iterate from 1 to the input number
while i <= number:
    # Initialize the inner loop counter
    j = 1
    
    # Inner loop: iterate from 1 to the input number
    while j <= number:
        # Print the multiplication result of i and j
        print(f"{i} x {j} = {i*j}")
        
        # Increment the inner loop counter
        j += 1
    
    # Increment the outer loop counter
    i += 1