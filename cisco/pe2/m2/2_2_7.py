"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 2 – The nature of strings in Python 
  7. Python strings are immutable
  8. Operations on strings: continued 
"""
alphabet = "bcdefghijklmnopqrstuvwxy"
print("Working on alphabet string", alphabet)

try:
    del alphabet[0]
except TypeError:
    print("Can't delete a char in a string, it is immutable!")

try:
    alphabet.append("A")
except AttributeError:
    print("Can't append to a string, it is immutable!")

try:
    alphabet.insert(0, "A")
except AttributeError:
    print("Can't insert in a string, it is immutable!")

alphabet = "a" + alphabet
alphabet = alphabet + "z"
print("Now alphabet referes to another string", alphabet)

# 8. operations
s = "aAbByYzZ"
print(f"On >{s}< the min char is >{min(s)}<")
print(f"On >{s}< the max char is >{max(s)}<")

s2 = 'The Knights Who Say "Ni!"'
print(f"On >{s2}< the min char is >{min(s2)}<")
print(f"On >{s2}< the max char is >{max(s2)}<")

t = [0, 1, 2]
print(f"On >{t}< the min integer is >{min(t)}<")
print(f"On >{t}< the min integer is >{max(t)}<")

s3 = "aAbByYzZaA"
print(f"Searching on {s3} by index")
print("Index of b is", s3.index("b"))
print("Index of Z is", s3.index("Z"))
print("Index of A is", s3.index("A"))

print("Using list() to split a string char by char:", end=' ')
print(list(s3))

print("Using count() on the string:")
print("Count 'a' is", s3.count("a"))
print("Count 'd' is", s3.count("d"))
