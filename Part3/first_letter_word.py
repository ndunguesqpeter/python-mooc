# Get a sentence from the user and store it in the 'sentence' variable
sentence = input("Please type in a sentence:")

# Initialize a variable 'index' to keep track of the current character position in the sentence
index = 0

# Loop through each character in the sentence
while index < len(sentence):
    # Check if the current character is the first character or if the previous character is a space
    if index == 0 or sentence[index - 1] == " ":
        # If the condition is met, print the current character (which is likely the first character of a word)
        print(sentence[index])
    
    # Move to the next character in the sentence
    index += 1