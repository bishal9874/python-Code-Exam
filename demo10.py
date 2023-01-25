from datetime import datetime

# Input dates
A = '1-10-2020'
B = '10-10-2020'

# Converting the dates to datetime objects
date1 = datetime.strptime(A, '%d-%m-%Y')
date2 = datetime.strptime(B, '%d-%m-%Y')

# Calculating the difference between dates
diff = date2 - date1

print("Number of days difference: ", diff.days)
