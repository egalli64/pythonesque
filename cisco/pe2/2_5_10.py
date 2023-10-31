"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 10. LAB Find a word!
 - Check if the chars in a string are (keeping the order) also in another string
    case insensitive
"""


def is_present(s, t):
    s = s.upper()
    t = t.upper()

    i = 0
    for c in s:
        j = t.find(c, i)
        if j == -1:
            return 'No'
        else:
            i = j + 1
    return 'Yes'


print(is_present('donor', 'Nabucodonosor'))  # Yes
print(is_present('donut', 'Nabucodonosor'))  # No
