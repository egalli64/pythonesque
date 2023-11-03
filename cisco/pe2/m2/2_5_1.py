"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 1. The Caesar Cipher: encrypting a message
 2. The Caesar Cipher: decrypting a message
"""


def caesar_cipher(text):
    result = ''
    for c in text:
        if c.isalpha():
            code = ord(c.upper()) + 1
            if code > ord('Z'):
                code = ord('A')
            result += chr(code)

    return result


sample = 'AVE CAESAR'
cipher = caesar_cipher(sample)
print(f'{sample} -> {cipher}')


def caesar_decipher(cipher):
    result = ''
    for c in cipher:
        if c.isalpha():
            code = ord(c.upper()) - 1
            if code < ord('A'):
                code = ord('Z')
            result += chr(code)
    return result


decipher = caesar_decipher(cipher)
print(f'{cipher} -> {decipher}')
