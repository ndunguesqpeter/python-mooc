hours = int(input("Enter hours (0-23): "))
minutes = int(input("Enter minutes (0-59): "))
add_minutes = int(input("Add how many minutes? "))

total_minutes = minutes + add_minutes
new_minutes = total_minutes % 60
extra_hours = total_minutes // 60
new_hours = (hours + extra_hours) % 24

print(f"new time: {new_hours:02d}:{new_minutes:02d}")