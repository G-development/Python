#Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.

import calendar

month = int(input("Insert month: "))
year = int(input("Insert year: "))

print(calendar.month(year, month))