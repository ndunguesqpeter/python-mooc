# Prompt the user to enter a string and store their input in the 'word' variable
word = input("Please type in a string: ")

# Print the length of the input string to the console
print(f"The length of the word is {len(word)}.")

# Initialize a counter variable to keep track of the current index
index = 1

# Loop until the index is greater than the length of the input string
while len(word) >= index:
    # Extract a slice of the input string from the start up to the current index
    slice = word[0:index]
    
    # Print the current index and the corresponding slice of the input string
    print(f"{index}:{slice}")
    
    # Increment the index for the next iteration
    index += 1