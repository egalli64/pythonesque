"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 6 - Exceptions once again
 3. Detailed anatomy of exceptions
"""


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)
