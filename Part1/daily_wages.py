# Daily wages
#Prompy, hourly wages, hours worked, day of the week
wages = float(input("Hourly wages:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
daily_wages = wages * hours
#Condition
if day == "Sunday":
    daily_wages *= 2
#Print daily wages
print(f"Daily wages:{daily_wages} euros")