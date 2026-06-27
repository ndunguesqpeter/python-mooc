# Prompt the user for a word and store their input
word = input("Word: ")

# Print a line of 30 asterisks to form the top border of a box
print("*" * 30)

# Calculate the number of spaces needed to center the word within the box
left = (28 - len(word)) // 2  # Calculate spaces to the left of the word
right = 28 - len(word) - left  # Calculate spaces to the right of the word

# Print the word centered within the box, surrounded by asterisks at the ends
print("*" + " " * left + word + " " * right + "*")

# Print another line of 30 asterisks to form the bottom border of the box
print("*" * 30)