input_string = input("Please type in a word:") 
substring = input("Please type in a character:")

# Check if substring is a single character
if len(substring) != 1:
    print("Please enter a single character.")
else:
    index = 0
    while index + 3 <= len(input_string):
        if input_string[index] == substring:
            print(input_string[index:index+3])
        index += 1