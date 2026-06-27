# Get user input and store it in the 'text' variable
text = input("Please type in a string:")

# Calculate the number of asterisks (*) needed to pad the text to a total length of 20 characters
# and store this padding in the 'command' variable
command = "*" * (20 - len(text))

# Print the padded text, with asterisks preceding the input text
print(f"{command}{text}")