#Comparison operators on strings
#ask for 2 words
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
#condition
if word2 > word1:
    print(f"{word2} comes alphabetically last.")
elif word1 > word2:
    print(f"{word1} comes alphabetically last.")
else:
    print("You gave the same word twice.")