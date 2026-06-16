# Get user input as a string and convert it to an integer
num = int(input("Please enter a number: "))

# Initialize a variable to store the result
result = num

# Check if the input number is negative
if num < 0:
    # If negative, make it positive by multiplying by -1
    result = num * -1

# Print the absolute value of the input number
print(f"The absolute value of this number is {result}")