# Get the number of rows from the user and convert it to an integer
row = int(input("Rows: "))

# Initialize a counter to track the current row being printed
initial = 1

# Continue printing rows until we've reached the desired number
while initial <= row:
    # Initialize a counter to track the current column being printed
    column = 1
    
    # Print numbers in the current row
    while column <= initial:
        # Print the current column number, followed by a space (not a newline)
        print(column, end=" ")
        # Move to the next column
        column += 1
    
    # Move to the next line after printing the current row
    print()
    
    # Move to the next row
    initial += 1