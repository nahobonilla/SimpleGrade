score = int(input("Enter your score (0-100): "))

grade = ""

if score >= 90:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is ", grade)