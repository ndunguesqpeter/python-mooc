# Get user input for a word and a character
word = input("Please type in a word: ")
character = input("Please type in a character: ")

# Initialize a counter variable to track the current index in the word
index = 0

# Loop through the word until there are less than 3 characters remaining
while index + 3 <= len(word):
    # Check if the character at the current index matches the input character
    if word[index] == character:
        # If it matches, print the 3-character substring starting at the current index
        print(word[index:index+3])
    # Move to the next character in the word
    index += 1