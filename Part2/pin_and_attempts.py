#the order of conditional stmts matters alot
attempts = 0
pin = "4321"
while True:
    trials = input("PIN:")
    attempts += 1
    
    print(f"Attempts:{attempts}")
    if trials == pin:
        if attempts == 1:
            print("Correct!It took only one single attempt!")
        else:
            print(f"Correct!It took you {attempts} attempts")
        break
    print("Wrong")