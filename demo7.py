List1 = [153,123,370,44]

# Creating an empty list to store Armstrong numbers
armstrong_numbers = []

# Iterating over the given list
for num in List1:
    # Converting the number to string to find its length
    num_string = str(num)
    num_length = len(num_string)

    # Initializing sum to zero
    sum_of_digits = 0

    # Iterating over each digit of the number
    for digit in num_string:
        sum_of_digits += int(digit) ** num_length

    # Checking if the number is an Armstrong number
    if sum_of_digits == num:
        armstrong_numbers.append(num)

# Finding the sum of Armstrong numbers
sum_of_armstrong_numbers = sum(armstrong_numbers)

print("Armstrong numbers: ", armstrong_numbers)
print("Sum of Armstrong numbers: ", sum_of_armstrong_numbers)
