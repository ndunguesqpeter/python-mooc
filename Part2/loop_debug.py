#This version acts strangely when user type in the correct PIN the 3rd attempt
attempts = 0
while True:
    print("The beginning of while loop")
    pin = input("please enter your PIN: ")
    attempts += 1
    
    print(f"Attempt: {attempts}")
    print("condition1:", attempts == 3)
    if attempts == 3:
        success = False
        break
    
    print("PIN:", pin)    
    print(f"condition2: {pin == 1234} ")
    if pin == "1234":
        success = True
        break
        
    print("Incorrect PIN...try again.")
if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")