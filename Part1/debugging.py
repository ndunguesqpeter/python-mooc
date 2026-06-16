#1. Hard-coding the problematic input
hourly_wage = 28
hours = 2
day = "sunday"

daily_wages = hourly_wage * hours
print("condition:", day == "sunday")
if day == "sunday":
#2. Debugging print statement before line doubling the daily wages
    print(daily_wages)
    daily_wages *= 2
# Debugging print statement after line doubling the daily wages
    print(daily_wages)

print(f"Daily wages: {daily_wages} euros")