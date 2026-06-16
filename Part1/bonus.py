#Loyality bonus calculation
points = int(input("How many points are on your card?"))
bonus = 1.15*points
#Condition to calculate bonus
if points < 100:
    bonus = 1.1*points
    print("Your bonus is 10%")
if points >= 100:
    print("Your bonus is 15%")
    bonus = 1.5*points
print(f"Your now have {bonus} points")
    