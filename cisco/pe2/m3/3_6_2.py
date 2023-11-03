"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 6 - Exceptions once again
 2. Exceptions are classes
"""
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())


def print_exception_tree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

class MyException(Exception):
    pass

print_exception_tree(BaseException)
