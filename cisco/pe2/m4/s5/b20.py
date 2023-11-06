"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 5 - The datetime module - working with time- and date-related functions
20. LAB The datetime and time modules
The script should get as input the datetime 2020, 11, 4, 14, 53 and output

2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
"""
from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
