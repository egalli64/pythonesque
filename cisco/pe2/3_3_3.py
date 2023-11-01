"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 3 – OOP: Properties
 3. Checking an attribute's existence
"""


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    print("No attribute 'b' in this object")

if hasattr(example_object, 'b'):
    print(example_object.b)
else:
    print("A cleaner way to detect if an object (or class) has a given attribute")