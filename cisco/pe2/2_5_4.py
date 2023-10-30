"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 4. The IBAN Validator (simplified)
"""


def validator(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        print("You have entered invalid characters.")
    elif len(iban) < 15:
        print("IBAN entered is too short.")
    elif len(iban) > 31:
        print("IBAN entered is too long.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        iban = int(iban2)
        if iban % 97 == 1:
            print("IBAN entered is valid.")
        else:
            print("IBAN entered is invalid.")


ibans = ['GB72 HBZU 7006 7212 1253 00',  # good
         'FR76 30003 03620 00020216907 50',  # good
         'DE02100100100152517108',  # good
         'FR76 30003 03620 00020216907 50 and something more',  # too long
         'FR76',  # too short
         '??02100100100152517108',  # invalid char
         'GB72 HBZU 7006 7212 1253 01',  # bad
         ]

for iban in ibans:
    print(iban, end=': ')
    validator(iban)
