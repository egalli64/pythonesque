"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 7. LAB Palindromes
 - empty string should not considered as a palindrome
 - case insensitive check
 - skip whitespaces
"""


def palindrome(text):
    text = text.replace(' ', '')

    if len(text) > 0 and text.upper() == text[::-1].upper():
        return "It's a palindrome"
    else:
        return "It's not a palindrome"

s1 = 'Ten animals I slam in a net'
print(f"'{s1}'.", palindrome(s1))  # yes

s2 = 'Eleven animals I slam in a net'
print(f"'{s2}'.", palindrome(s2))  # yes
