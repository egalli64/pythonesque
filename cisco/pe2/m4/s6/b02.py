"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 6 - The calendar module - working with calendar-related functions
 1. Introduction to the calendar module
 2. Your first calendar
 3. Calendar for a specific month
 4. The setfirstweekday() function
 5. The weekday() function
 6. The weekheader() function
 7. How do we check if a year is a leap year?
"""
import calendar

print(calendar.calendar(2023))

print("---")
calendar.prcal(2023)

print("---")
print(calendar.month(2023, 11))

print("---")
calendar.setfirstweekday(calendar.WEDNESDAY)
calendar.prmonth(2023, 11)

print("\nXmas 2023 is on:", calendar.weekday(2023, 12, 25))

for i in range(5):
    print(f"Week header {i} is:", calendar.weekheader(i))

print("Is 2020 a leap year?", calendar.isleap(2020))
print("How many leap years in [2010, 2021)?", end=" ")
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.
