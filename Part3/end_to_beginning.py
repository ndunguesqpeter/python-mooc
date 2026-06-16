input_string = input("Please type in a string: ")
index = -1
#Condition
while index >= -len(input_string):
    print(f"{input_string[index]}")
    #Update variables
    index -= 1