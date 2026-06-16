# Get user input and store it as an integer
num = int(input("Enter number : "))

# Loop over each row of the pattern
for row in range(1, num + 1):
    # For each row loop over each column
    for col in range(1, num + 1):
        # If the sum of the row and column is even, print "1"
        if (row + col) % 2 == 0:
            print("1", end="") # Print "1" followed by a space, without a newline
            # If the sum is odd, print "0"
        else:
            print("0", end="")# Print "0" followed by a space, without a newline
            # Move to the next line after printing each row
    print()