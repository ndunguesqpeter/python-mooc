# Program to find the letter in the middle
# Initialization
a = input("First: ")
b = input("Second: ")
c = input("Third: ")

# Condition 
# 1st condition "a" is the lagest
if a > b and a > c:
    if b > c:
        middle = b
    else:
        middle = c
# 2nd condition "b" is the largest:
#This elif triggers when a is NOT the largest. Compare "b" & "c" since "a" is not the largest.
elif c > b:
    if b > a:
        middle = b
    else:
        middle = a
# 3rd condition "c" is the largest
# This means else triggers if neither "a" or "b" is the largest. 1st & 2nd condition.
else:
    if c > a:
        middle = c
    else:
        middle = a

# Print output
print(f"The letter in the middle is {middle}.")