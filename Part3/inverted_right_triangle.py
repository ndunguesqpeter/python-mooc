# Get the number of rows from the user and convert it to an integer
row = int(input("Rows: "))
# Initialize the number of columns to 0
column = 0

# Continue the loop as long as the number of rows is greater than 0
while row > 0:
    # Print a line consisting of '*' characters followed by ' ' characters
    # The number of '*' characters decreases by 1 in each iteration
    # The number of ' ' characters increases by 1 in each iteration
    print((row*"*") + (column*" "))
    # Increment the number of columns by 1
    column += 1
    # Decrement the number of rows by 1
    row -= 1