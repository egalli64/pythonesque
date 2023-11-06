"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 6 - The calendar module - working with calendar-related functions
 8. Classes for creating calendars
 9. Creating a Calendar object
10. The itermonthdates() method
11. Other methods that return iterators
12. The monthdays2calendar() method
"""
import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
print()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
print()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
print()

for data in c.monthdays2calendar(2020, 12):
    print(data)
