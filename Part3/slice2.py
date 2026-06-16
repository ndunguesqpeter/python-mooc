# Write your solution here
word = input("Please type in a string:")
end = len(word) - 1
while end >= 0:
    print(word[end:])
    end -= 1   

"""
Code Explanation
Here's a line-by-line breakdown of your code:

string = input("Please type in a string: ")

This line prompts the user to enter a string and stores their input in the string variable.
start = len(string) - 1

This line calculates the index of the last character in the string.
In Python, indices start at 0, so the last index is length - 1.
while start >= 0:

This line starts a while loop that continues as long as start is greater than or equal to 0.
The loop will iterate over the indices of the string in reverse order.
print(string[start:])

Inside the loop, this line prints a slice of the string starting from the current start index to the end of the string.
This effectively prints the suffixes of the input string in reverse order.
start -= 1

This line decrements the start index by 1 in each iteration, moving to the previous character in the string.
Example Walkthrough
If the user inputs "hello", the code will output:


Visualize Me
"""