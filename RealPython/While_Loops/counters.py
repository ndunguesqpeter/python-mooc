# Initialize Helper Variable
attempts = 0

# Check helper variable condition
while attempts < 3:
    pin = input("enter a 4-digit PIN: ")
    if pin == "1234":
        print("Access granted!")
        break # Exit the loop immediately
    else:
        print("Incorrect PIN.")
    
    # Modify helper variable
    attempts += 1

if attempts == 3:
    print("Account locked due to too many failed attempts.")