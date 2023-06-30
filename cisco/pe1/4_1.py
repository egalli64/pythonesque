"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 1 – Functions
"""
# a function must be defined before being invoked
try:
    hi()
except NameError:
    print("Move function defnition _before_ function invokation!")


def hi():
    print("hi!")


# function invocation must match function definition
try:
    hi(5)
except TypeError:
    print("This function does not require any argument")
