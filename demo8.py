a = 'python 3.9'
b = 'python 2.7'

# Extracting numbers from the string
num1 = ''
num2 = ''
for i in a:
    if i.isdigit() or i == '.':
        num1 += i
for i in b:
    if i.isdigit() or i == '.':
        num2 += i

num1 = float(num1)
num2 = float(num2)

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
