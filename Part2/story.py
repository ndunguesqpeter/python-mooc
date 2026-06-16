next = ""
words = 0

while True:
    word = input("Please type in a word: ")
    
    if word == "end":
        break
    words += 1
    next += word + " "
print(next)