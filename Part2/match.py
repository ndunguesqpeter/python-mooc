#If more than two option in the program use elif
home = int(input("Home goals scored: "))
away = int(input("Away goals scored: "))
#condition
if home > away:
    print("The home team won!")
elif away > home:
    print("The away team won!")
else:
    print("It's a tie!")