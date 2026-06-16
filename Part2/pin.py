while True:
    code = input("Please type in your PIN: ")
    tries = 3
    if code == "1234":
        break
    print("Incorrect...try again")
    
    if tries == 3:
        tries +=1
print("Correct PIN entered!")