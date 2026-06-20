# Initialize an empty string to store the input words and a counter for the number of words
next_words = ""  # Renamed 'next' to 'next_words' to avoid using a built-in Python keyword
words = 0

# Create an infinite loop that will continue until the user types "end"
while True:
    # Prompt the user to input a word
    word = input("Please type in a word: ")
    
    # Check if the user has typed "end" to exit the loop
    if word == "end":
        break  # Exit the loop when "end" is typed
    
    # Increment the word counter
    words += 1
    
    # Append the input word to the string of words
    next_words += word + " "

# Print the string of words after the loop exits
print(next_words)