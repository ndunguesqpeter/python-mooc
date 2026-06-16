#Define the number of rows
num = 5
#Outer loop to iterate the rows
for row in range(1, num + 1):
    start = (num - row)
    # This line prints start number of spaces without moving to a new line (end="" prevents a newline).
    print(" " * start, end="")
    col_range = row - 1
    # This line calculates a value that is used to determine the number of characters 
    # (asterisks and spaces) to print in the current row.
    for col in range(row + col_range):
        # This line starts another for loop that will iterate row + column_range times. 
        # The loop variable col takes on values from 0 to row + column_range - 1.
        if col % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()
    """
    # Define the number of rows for the pattern
num = 5

# Outer loop to iterate over each row in the pattern
for row in range(1, num + 1):
    # Calculate the number of spaces to print before the pattern in the current row
    start = num - row
    
    # Print the required number of spaces without moving to a new line
    print(" " * start, end="")

    # Calculate the total number of characters (asterisks and spaces) to print in the current row
    col_range = row - 1
    
    # Inner loop to print asterisks and spaces in the current row
    for col in range(row + col_range):
        # Alternate between asterisks and spaces based on the column index
        if col % 2 == 0:
            # Print an asterisk if the column index is even
            print("*", end="")
        else:
            # Print a space if the column index is odd
            print(" ", end="")
    
    # Move to a new line after printing each row
    print()
    The code generates a pattern of asterisks and spaces, 
    with the number of rows determined by the value of num. 
    The pattern is symmetrical and has a specific structure.
    """