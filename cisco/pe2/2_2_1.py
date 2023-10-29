"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 2 – The nature of strings in Python
"""
word = 'by'
print(f"A short string >{word}< with length {len(word)}")

empty = ''
print(f"An empty string >{empty}< has length {len(empty)}")

multiline = '''Line #1
Line #2'''

print("A multiline string, sized", len(multiline))
print(multiline)
print("White spaces and newline are counted as a char")

print("Overload of + and * for strings")
str1 = 'a'
str2 = 'b'

print(f"{str1} + {str2} is", str1 + str2)
print(f"{str2} + {str1} is", str2 + str1)
print(f"5 * {str1} is", 5 * str1)
print(f"{str2} * 4 is", 'b' * 4)

char_1 = 'a'
ord_1 = ord(char_1)
print(f"As char is >{char_1}<, its ASCII ordinal number is {ord_1} ")
print(f"As integer is >{ord_1}<, as char is {chr(ord_1)} ")
char_2 = ' '
ord_2 = ord(char_2)
print(f"As char is >{char_2}<, its ASCII ordinal number is {ord(char_2)} ")
print(f"As integer is >{ord_2}<, as char is {chr(ord_2)} ")
char_3 = 'α'
ord_3 = ord(char_3)
print(f"As char is >{char_3}<, its ASCII ordinal number is {ord(char_3)} ")
print(f"As integer is >{ord_3}<, as char is {chr(ord_3)} ")
