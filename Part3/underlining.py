# loop. print out each string underlined 
while True:
    string = input("Please type in a string:")
#Condition
    if string == "":
        break
    print(string)
    print("-" * len(string))