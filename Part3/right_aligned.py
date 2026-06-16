text = input("Please type in a string:")
command = "*" * (20 - len(text))
print(f"{command}{text}")