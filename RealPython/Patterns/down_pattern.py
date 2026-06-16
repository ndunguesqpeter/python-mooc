# Ask the user to input a number and convert it to an integer
num = int(input("Number: "))

# Loop through each row in the pattern, from 0 to the input number
for row in range(1, num + 1):
    # For each row, loop through each column, printing the row number 'row' times
    for col in range(1, row + 1):
        # Print the current row number without starting a new line
        print((row), end="")
        # Start a new line after printing each row
    print("")