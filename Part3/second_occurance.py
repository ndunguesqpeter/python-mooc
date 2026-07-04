# Ask the user for a word and a character to search for within that word
word = input("Please type in a word: ")
character = input("Please type in a character: ")

# Initialize variables to keep track of the current index and the number of occurrences
index = 0
occurrences = 0

# Loop through the word until we've checked all characters
while index < len(word):
    # Check if the substring starting at the current index matches the character
    if word[index:index + len(character)] == character:
        # If it matches, increment the occurrences counter
        occurrences += 1
        # If this is the second occurrence, print the index and stop the loop
        if occurrences == 2:
            print(f"The second occurrence of the substring is at index {index}.")
            break
        # Move the index forward by the length of the character (to avoid re-checking the same substring)
        index += len(character)  # Removed unnecessary parentheses
    else:
        # If it doesn't match, move the index forward by one character
        index += 1
else:
    # If the loop completes without finding a second occurrence, print a message indicating this
    print("The substring does not occur twice in the string.")