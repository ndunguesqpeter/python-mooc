# Define the number of rows in the pattern
num = int(input("Number: "))

# Initialize row counter
row = 1

# Loop over each row in the pattern
while row <= num:
    # Calculate the number of spaces to print before the asterisks
    start = num - row
    
    # Print the required number of spaces without starting a new line
    print(" " * start, end="")
    
    # Initialize column counter
    col = 1
    
    # Loop over the number of asterisks to print in the current row
    while col <= row:
        # Print an asterisk without starting a new line
        print("*", end="")
        col += 1
    
    # Start a new line after printing the current row
    print("")
    
    # Move to the next row
    row += 1