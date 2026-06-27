# Initialize a variable to store the input word
word = "Python"

# Initialize an empty string to store the reversed word
result = ""

# Initialize an index variable to start from the end of the word
# -1 is the index of the last character in the word
index = -1

# Continue the loop as long as the index is within the bounds of the word
while index >= -len(word):
    # Append the character at the current index to the result string
    result += word[index]
    
    # Print the current state of the result and the index for debugging purposes
    print(f"{result}:{index}")
    
    # Move the index to the previous character in the word
    index -= 1