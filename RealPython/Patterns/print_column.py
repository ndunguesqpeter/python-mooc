# Set the number of rows for the pattern
num = 5
# If you want the user to enter the number of rows, uncomment the below line
# rows = int(input('Enter the number of rows'))

# Outer loop to iterate over each row
for row in range(1, num + 1): 
    # Nested loop to print the row number for each column in the current row
    for col in range(1, row + 1):
        # Print the current row number, followed by a space (not a newline)
        print(row, end=" ")
    
    # Print a newline to move to the next row
    print()