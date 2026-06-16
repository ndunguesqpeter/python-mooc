# Define the number of rows in the pattern
num = int(input("Number: "))

# Loop over each row in the pattern
for row in range(1, num + 1):
    # Calculate the number of spaces to print before the asterisks
    start = num - row
    
    # Print the required number of spaces without starting a new line
    print(" " * start, end="")
    
    # Loop over the number of asterisks to print in the current row
    for col in range(row):
        # Print an asterisk without starting a new line
        print("*", end="")
    
    # Start a new line after printing the current row
    print("")