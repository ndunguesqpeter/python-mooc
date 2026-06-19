total = 0
entered_numbers = []

user_iput = ""

while user_iput != "stop":
    user_iput = input("enter a number to add (or 'stop' to calculate): ")
    
    if user_iput.isdigit():
        number = int(user_iput)
        
        total += number
        entered_numbers.append(number)
print(f"You entered: {entered_numbers}")
print(f"The final sum is: {total}")