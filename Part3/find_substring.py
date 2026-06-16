input_string = input("Please type in a word:")

substring = input("Please type in a character:")
index = input_string.find(substring)
if index!=-1 and index <= len(input_string) - 3:
    print(input_string[index:index+3]) 
    
"""
Code Breakdown
Here's a step-by-step explanation of the code:

input_string = input("Please type in a word:")

This line asks the user to enter a word and stores the input in the input_string variable.
substring = input("Please type in a character:")

This line asks the user to enter a character and stores the input in the substring variable.
index = input_string.find(substring)

The find() method is used to get the index of the first occurrence of substring in input_string.
If substring is not found, find() returns -1, and this value is stored in the index variable.
if index <= len(input_string) - 3:

This line checks if the index of substring is such that there are at least 3 characters remaining in input_string from index onwards.
It ensures that slicing input_string from index to index + 3 will not result in an "index out of range" error.
print(input_string[index:index+3])

If the condition is true, this line prints a substring of input_string starting from index and having a length of 3.
Example Walkthrough
Using the provided user inputs:

"mammoth"
"m"
input_string becomes "mammoth".
substring becomes "m".
index becomes 0 because "m" is found at index 0 in "mammoth".
The condition index <= len(input_string) - 3 is true because 0 <= 7 - 3 is 0 <= 4, which is true.
print(input_string[index:index+3]) prints "mam" because input_string[0:3] is "mam".
"""
   