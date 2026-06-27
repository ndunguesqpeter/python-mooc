# Prompt the user for a word and store their input
word = input("Please type in a string: ")

# Print the length of the input string
print(f"The length of the word is {len(word)}.")

# Store the length of the word for later use
length = len(word)

# Start at the last index of the word
index = length - 1

# Loop through the word in reverse order
while index >= 0:
    # Get a slice of the word from the current index to the end
    slice = word[index:length]
    # Print the current index and the corresponding slice
    print(f"{index}:{slice}")
    # Move to the previous index
    index -= 1