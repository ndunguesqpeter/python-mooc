# Get user input and store it in the variable input_string
input_string = input("Please enter a string: ")
# Initialize index to -1, which corresponds to the last character of the string
index = -1

# Continue the loop as long as the index is greater than the negative length of the string
while index > -len(input_string):
    # Print the character at the current index and its index
    print(f"{input_string[index]}: {index}")
    # Decrement the index to move to the previous character
    index -= 1
print(input_string[::-1])