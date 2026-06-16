string = input("Please type in a string:")
length = (string + "*" * (20 - len(string)) )
print("The length of the string is " + str(len(length)))
print(length)