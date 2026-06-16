# Program to find the letter in alphabetical order that is in the middle of three input letters

# Get three letters from the user
a = input("First letter: ")  # store the first letter
b = input("Second letter: ")  # store the second letter
c = input("Third letter: ")   # store the third letter

# Determine the middle letter by comparing the three input letters
# 1st condition: "a" is the largest letter
if a > b and a > c:  # check if "a" is greater than both "b" and "c"
    if b > c:  # if "a" is largest, compare "b" and "c" to find the middle letter
        middle = b  # "b" is the middle letter if it's greater than "c"
    else:
        middle = c  # "c" is the middle letter if it's greater than "b"

# 2nd condition: "b" is the largest letter (implies "a" is not the largest)
elif b > c:  # check if "b" is greater than "c"
    if c > a:  # if "b" is largest, compare "c" and "a" to find the middle letter
        middle = c  # "c" is the middle letter if it's greater than "a"
    else:
        middle = a  # "a" is the middle letter if it's greater than "c"

# 3rd condition: "c" is the largest letter (implies "a" and "b" are not the largest)
else:  # "c" is the largest letter
    if b > a:  # compare "b" and "a" to find the middle letter
        middle = b  # "b" is the middle letter if it's greater than "a"
    else:
        middle = a  # "a" is the middle letter if it's greater than "b"

# Print the middle letter
print(f"The letter in the middle is {middle}.")