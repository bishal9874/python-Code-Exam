dt = {'rohit':[55,56,67], 'lisha':[66,89,74],'angel':[98,84,88],'sam':[88,85,79]}

# Grading system
grades = {
    'A': (80, 100),
    'B': (60, 80),
    'C': (45, 60),
    'D': (35, 45),
    'F': (0, 35)
}

# List to store A graded students
result = []

for student, marks in dt.items():
    # Finding the average of marks
    avg = sum(marks) / len(marks)

    # Assigning grade to the candidate
    for grade, (min_mark, max_mark) in grades.items():
        if min_mark <= avg <= max_mark:
            student_grade = grade
            if grade == 'A':
              result.append(student)
            break
    print(f'{student} got grade {student_grade} with average {avg}')

#Printing the A graded students
print(result)
