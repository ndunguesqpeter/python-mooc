#Which string is longer than the other?
#Initialization
string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")

#Condition
if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")