next = ""
end = ""
while True:
    word = input("Please type a word: ")
    if word == end:
        break
    next += word + " "
    end = word
print(next)