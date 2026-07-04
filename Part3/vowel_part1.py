# Get a string input from the user
text = input("Please type in a string: ").lower()  # convert to lowercase for case-insensitive comparison

# Define a string of vowels to check for in the input
vowels = "aeiou"  # also checking for 'i' and 'u'
# Initialize an index to keep track of the current vowel being checked
index = 0

# Loop through each vowel in the 'vowels' string
while index < len(vowels): 
    # Get the current vowel based on the 'index'
    vowel = vowels[index] 
    # Check if the current vowel is present in the user's input
    count = text.count(vowel)  # count the occurrences of the vowel
    if count > 0:
        # If the vowel is found, print the count
        print(f"{vowel} found {count} time{'s' if count > 1 else ''}")
    else:
        # If the vowel is not found, print a failure message
        print(f"{vowel} not found")
    # Move to the next vowel by incrementing the 'index'
    index += 1