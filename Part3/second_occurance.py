word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
occurrences = 0
 
while index < len(word):
    if word[index:index + len(character)] == character:
        occurrences += 1
        if occurrences == 2:
            print(f"The second occurrence of the substring is at index {index}.")
            break
        index += (len(character))
    else:
        index += 1
else:
    print("The substring does not occur twice in the string.")  