words = ""
attempts = 0

while True:
    word = input("Please type in a word:")
    
    if word == "end":
        break
    attempts += 1
    words += word + " "
print(f"The number of words entered is {attempts}.")
print(f"My story goes like: {words}")