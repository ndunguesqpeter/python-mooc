# Two helper variables; attempts(keeps track how many times user typed PIN)
#success(set to True/False based on whether the user is successful in signing in)

attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    if code == "1234":
        success = True
        break
    if attempts == 3:
        success = False
        break
    print("Incorrect...try again.")
if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
    '''
    The loop is exited either when the user types the correct PIN or if there
    have been too many attempts. the if statement after the loop checks the value 
    of the variable success and prints out a message accordingly.
    '''
    