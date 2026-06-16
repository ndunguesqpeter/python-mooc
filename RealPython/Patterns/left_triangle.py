# Define the number of rows in the pattern
num = int(input("Number: "))

# Loop over each row in the pattern
for row in range(1, num + 1):
    # Print an asterisk without starting a new line
    print("*" * row)