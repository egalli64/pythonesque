"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 6. LAB Improving the Caesar cipher
 - shift could be in [1 .. 25]
 - preserve the letters' case
 - non-alphabetical characters should remain untouched
"""
def caesar_cipher(text, shift):
    # default shift to 1
    if shift not in range(1, 26):
        shift = 1

    result = ''
    for c in text:
        if c.isalpha():
            first = ord('A') if c.isupper() else ord('a')
            code = (ord(c) + shift - first) % 26
            result += chr(first + code)
        else:
            result += c

    return result

print(caesar_cipher('abcxyzABCxyz 123', 2))
print(caesar_cipher('The die is cast', 25))
