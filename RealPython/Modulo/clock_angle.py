hours = int(input("Enter hours (1-12): "))
minutes = int(input("Enter minutes (0-59): "))

hours_angle = (hours % 12) * 30 + minutes * 0.5
minute_angle = minutes * 6
diff = abs(hours_angle - minute_angle)

print(f"Angle between hands: {min(diff, 360 - diff)} degrees")