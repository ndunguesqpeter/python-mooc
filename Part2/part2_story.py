# Initialize variables to store the concatenated string and the last input word
next_str = ""  # Renamed to avoid using a built-in keyword
end = ""

# Loop indefinitely until a specific condition is met
while True:
    # Prompt the user to input a word
    word = input("Please type a word: ")
    
    # Check if the input word is the same as the previous one
    if word == end:
        # If they are the same, exit the loop
        break
    
    # Concatenate the input word to the result string with a space
    next_str += word + " "
    
    # Update the 'end' variable with the current input word for the next iteration
    end = word

# Print the concatenated string after the loop exits
print(next_str.strip())  # Added strip() to remove trailing whitespace