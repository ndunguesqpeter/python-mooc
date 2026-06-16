words = ""
previous = ""

while True:
    word = input("Please type in a word:")
    
    if word == "end" or word == previous:
        break
    
    words += word + " "
    previous = word
print(f"My story goes like: {words}")