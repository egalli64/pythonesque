"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 6 – Errors, the programmer's daily bread
 1. Errors, failures, and other plagues
 2. Exceptions
"""
import math

values = [25, 'mistake', -1, 4.5, 0]

for value in values:
    try:
        print(f"Square root of >{value}< is", math.sqrt(value))
    except:
        print("Can't get square root of", value)

try:
    value = 1
    value /= 0
except:
    print("Can't divide by zero")

try:
    my_list = []
    print(my_list[0])
except:
    print("Can't access an out of bounds array element")

print("Different exceptions")
for value in values:
    try:
        x = int(value)
        y = 1 / x
        print(y)
    except ZeroDivisionError:
        print("You cannot divide by zero, sorry.")
    except ValueError:
        print("You must enter an integer value.")
    except:
        print("Oh dear, something went wrong...")
