attempts = 3

while True:
    code = input("Please enter the PIN: ")
    attempts += 1
    
    if code == "1234":
        success = True
        break
    if attempts == 3:
        success = False
        break
    print("Incorrect...Try Again!")
 
if success:
    print("Correct PIN entered!")
else:
    print(f"Too many attempts. You used all {attempts} attempts!")