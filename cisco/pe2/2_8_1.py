"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 8 – Useful exceptions
 1. Built-in exceptions
"""
import time

data = [1, 2, 3, 4, 5]
i = 0
good = True

while good:
    try:
        print(data[i])
        i += 1
    except IndexError:
        good = False

print('Done')


seconds = 0

while seconds < 10:
    try:
        print(seconds)
        seconds += 1
        time.sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
