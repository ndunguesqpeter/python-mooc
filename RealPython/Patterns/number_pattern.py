# Define the number of rows for the pattern
num = 6
# If you want to get the number of rows from the user, uncomment the line below
# rows = int(input('Enter the number of rows'))

# Outer loop to iterate over each row
for row in range(num):
    # Nested loop to print numbers in the current row
    for col in range(row):
        # Print the current row number, followed by a space (not a newline)
        print(row, end=" ")
    
    # Print a newline to move to the next row
    print()
    
    """
In this number pattern, we display a single digit on the first row, 
two digits on the second row, and three digits on the third row. 
This process will repeat until the number of rows is reached.
Note:
The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
    """