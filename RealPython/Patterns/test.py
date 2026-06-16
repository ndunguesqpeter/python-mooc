# Ask the user for the number of rows in the pattern and store it in 'num'
# The input is currently hardcoded to 5, but can be uncommented to get user input
num = 5 # int(input("Number: "))

# Loop through each row in the pattern, starting from 1 and going up to 'num'
for row in range(1, num + 1):
    # Calculate the number of leading spaces needed for this row
    start = (num - row)
    
    # Print the leading spaces for this row
    print(" " * start, end="")
    
    # Loop through each column in the row, printing alternating asterisks and spaces
    for col in range(2 * (row - 1)):
        # Check if the column index is even
        if col % 2 == 0:
            # If even, print an asterisk
            print("*", end="")
        else:
            # If odd, print a space
            print(" ", end="")  
    
    # Move to the next line after printing the row
    print("")