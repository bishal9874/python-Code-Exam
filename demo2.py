#Input List
List1 = [19,12,2021]

#Converting the values in list to date time object
date_object = f'{List1[0]}-{List1[1]}-{List1[2]}'

#Getting the date
date = date_object

#Getting the month name
month_name = date_object.split("-")[1]

#Getting the day of week
day_of_week = date_object.split("-")[0]

print("Date: ", date)
print("Month: ", month_name)
print("Day of Week: ", day_of_week)
