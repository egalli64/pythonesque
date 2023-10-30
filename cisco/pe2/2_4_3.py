"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 4 – String in action
 3. Strings vs. numbers
"""
i1 = 13
f1 = 1.3
si1 = str(i1)
sf1 = str(f1)

print("Explicit conversion to string by str:", si1, sf1)

print("Back to number by int() and float():", int(si1), float(sf1))

try:
    print(int(sf1))
except ValueError:
    print("Be careful using int() and float()")
