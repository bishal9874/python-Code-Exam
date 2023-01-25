M1 = 40
M2 = 48
M3 = 88

# Assigning grades to individual marks
if M1 < 25:
    grade1 = 'F'
elif M1 >= 25 and M1 <= 45:
    grade1 = 'E'
elif M1 > 45 and M1 <= 50:
    grade1 = 'D'
elif M1 > 50 and M1 <= 60:
    grade1 = 'C'
elif M1 > 60 and M1 <= 80:
    grade1 = 'B'
else:
    grade1 = 'A'

if M2 < 25:
    grade2 = 'F'
elif M2 >= 25 and M2 <= 45:
    grade2 = 'E'
elif M2 > 45 and M2 <= 50:
    grade2 = 'D'
elif M2 > 50 and M2 <= 60:
    grade2 = 'C'
elif M2 > 60 and M2 <= 80:
    grade2 = 'B'
else:
    grade2 = 'A'

if M3 < 25:
    grade3 = 'F'
elif M3 >= 25 and M3 <= 45:
    grade3 = 'E'
elif M3 > 45 and M3 <= 50:
    grade3 = 'D'
elif M3 > 50 and M3 <= 60:
    grade3 = 'C'
elif M3 > 60 and M3 <= 80:
    grade3 = 'B'
else:
    grade3 = 'A'

# Calculating the average of marks
average = (M1 + M2 + M3) / 3

# Assigning total grade
if average < 25:
    total_grade = 'F'
elif average >= 25 and average <= 45:
    total_grade = 'E'
elif average > 45 and average <= 50:
    total_grade = 'D'
elif average > 50 and average <= 60:
    total_grade = 'C'
elif average > 60 and average <= 80:
    total_grade = 'B'
else:
    total_grade = 'A'

print("Grade for M1: ", grade1)
print("Grade for M2: ", grade2)
print("Grade for M3: ", grade3)
print("Average of marks: ", average)
print("Total grade: ", total_grade)
