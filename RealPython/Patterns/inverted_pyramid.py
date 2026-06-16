# Define the number of rows in the pattern
num = 5

# Outer loop to iterate over each row
for row in range(1, num + 1):
    # Inner loop to print numbers in the current row
    # The number of elements in each row decreases as 'row' increases
    for col in range((num - row) + 1):
        # Print the current row number, followed by a space (instead of a newline)
        print("*", end=" ")
    # Move to the next line after printing all elements in the current row
    print()