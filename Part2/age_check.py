#testinf and and or operator in combining conditions
#input
age = int(input("What is your age? "))
if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite well yet...")
else:
    print(f"Ok, you're {age} years old")