#Which string is longer than the other?
#Initialization
string = input("Please type in a string:")
str1 = string[1]
str2 = string[-2]

#Condition
if str1 != str2:
    print(f"The second and the second to last characters are different")
elif str1 == str2:
    print(f"The second and the second to last characters are {str1}")