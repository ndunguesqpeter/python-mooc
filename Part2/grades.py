# Prompt the user to input the number of points and convert it to an integer
points = int(input("How many points [0-100]: "))

# Check if the input points are within the valid range (0-100)
if points < 0 or points > 100:
    # If not, set the grade to "Impossible"
    grade = "Impossible"
# Check the grade based on the points, using the given grading scale
elif points < 50:   # Less than 50 points is a fail
    grade = "fail" 
elif points < 60:   # 50-59 points is grade 1
    grade = "1"
elif points < 70:   # 60-69 points is grade 2
    grade = "2"
elif points < 80:   # 70-79 points is grade 3
    grade = "3"
elif points < 90:   # 80-89 points is grade 4
    grade = "4"
else:               # 90 or more points is grade 5
    grade = "5"

# Print the determined grade
print(f"Grade: {grade}")