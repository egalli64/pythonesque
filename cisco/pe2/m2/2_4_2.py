"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 4 – String in action
 2. Sorting
"""
greek = ['omega', 'alpha', 'pi', 'gamma']
greek_2 = sorted(greek)
print("Original list", greek)
print("Sorted list", greek_2)

greek.sort()
print("Original list, after sort()", greek)
