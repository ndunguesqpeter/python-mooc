shopping_list = ""
items = 0

while True:
    item = input("Enter an item (or 'done' to finish): ")
    
    if item == "done":
        break
    
    items += 1
    shopping_list += item + ", "

print(f"You entered {items} items.")
print(f"Your shopping list: {shopping_list}")