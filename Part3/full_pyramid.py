# Get the number of rows from the user
row = int(input("Rows: "))

# Initialize the pattern to be printed
pattern = "*"  

# Continue printing the pattern until the number of rows reaches 0
while row > 0:
    # Print the pattern indented with spaces, where the number of spaces decreases with each row
    print(row*" " + pattern)
    # Increase the width of the pattern by 2 asterisks for the next row
    pattern += "**"
    # Decrement the row counter
    row -= 1