word = input("Word:")
print("*" * 30)
left = (28 - len(word)) // 2
right = left
if len(word) % 2 != 0:
    right += 1
print("*" + left * " " + word + " "*right + "*")
print("*" * 30)   