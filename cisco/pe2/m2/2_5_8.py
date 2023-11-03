"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 8. LAB Anagrams
 - two empty strings are not anagrams
 - case insensitive
 - skip whitespaces
"""


def anagrams(s1, s2):
    l1 = sorted(list(s1.replace(' ', '').upper()))
    l2 = sorted(list(s2.replace(' ', '').upper()))

    if len(l1) > 0 and l1 == l2:
        return "Anagrams"
    else:
        return "Not anagrams"


print(anagrams('Listen', 'Silent'))  # yes
print(anagrams('modern', 'norman'))  # no
print(anagrams('', ''))  # no
