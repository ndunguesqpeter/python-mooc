# Get user input and convert it to an integer
number = int(input("Please type in a number:"))

# Initialize the outer loop counter
counter1 = 1

# Outer loop: iterate from 1 to the input number
while counter1 <= number:
    # Initialize the inner loop counter
    counter2 = 1
    
    # Inner loop: iterate from 1 to the input number
    while counter2 <= number:
        # Print the multiplication result of i and counter2
        print(f"{counter1} x {counter2} = {counter1*counter2}")
        
        # Increment the inner loop counter
        counter2 += 1
    
    # Increment the outer loop counter
    counter1 += 1