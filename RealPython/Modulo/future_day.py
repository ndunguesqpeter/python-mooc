days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start_day = int(input("Starting day (0=Sun, 1=Mon, ...6=Sat): "))
days_ahead = int(input("How many days ahead? "))

future_day = (start_day + days_ahead) % 7
print(f"After {days_ahead} days, it will be: {days[future_day]}")