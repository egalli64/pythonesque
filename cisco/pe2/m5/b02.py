"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 5 - The datetime module - working with time- and date-related functions
 1. Introduction to the datetime module
 2. Getting the current local date and creating date objects
 3. Creating a date object from a timestamp
 4. Creating a date object using the ISO format
 5. The replace() method
 6. What day of the week is it?
"""
from datetime import date
import time

# local date
today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

my_date = date(2019, 11, 4)
print("A date:", my_date)

# timestamp
timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

# replace - dates are read-only, it creates a new date
replaced = d.replace(year=1992, month=1, day=16)
print(d, replaced)

# weekday
print("The 'd' weekday [0..6] is", d.weekday())
print("The 'd' ISO weekday [1..7] is", d.isoweekday())