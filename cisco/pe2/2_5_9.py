"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 9. LAB The Digit of Life
 - Sum up all the digits in the passed string to get a single digit as result
"""


def life(s):
    if len(s) != 8 or not s.isdigit():
        return 0

    result = int(s)
    while result > 9:
        last = result % 10
        result //= 10
        result += last
    return result


print(life('19991229'))  # 6
print(life('20000101'))  # 4
