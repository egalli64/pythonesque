"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 3 – LAB Your own split
"""


def my_split(s):
    result = []

    buffer = ''
    for c in s:
        if c.isspace():
            if len(buffer) > 0:
                result.append(buffer)
            buffer = ''
        else:
            buffer += c

    if len(buffer) > 0:
        result.append(buffer)

    return result


print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
