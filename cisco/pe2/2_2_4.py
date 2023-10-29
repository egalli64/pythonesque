"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 2 – The nature of strings in Python 
  4. Strings as sequences
  5. Slices
  6. The in and not in operators 
"""
the_string = 'silly walks'
print(f"Accessing each char in >{the_string}< by index:", end=' ')

for i in range(len(the_string)):
    print(the_string[i], end=' ')
print()

print(f"Iterating on >{the_string}< char by char:", end=' ')
for c in the_string:
    print(c, end=' ')
print()

alpha = "xabcdefg"
print("Slicing", alpha)

print("Slice [1 .. 3)", alpha[1:3])
print("Slice [3 ..)", alpha[3:])
print("Slice [.. 3)", alpha[:3])
print("Slice [5 .. -2)", alpha[5:-2])
print("Slice [-3 .. 6)", alpha[-3:6])
print("Slice :: (copy)", alpha[::])
print("Slice ::2", alpha[::2])
print("Slice 1::2", alpha[1::2])

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Check if a string is in / not in", alphabet)

print("Is f in?", "f" in alphabet)
print("Is F in?", "F" in alphabet)
print("Is 1 in?", "1" in alphabet)
print("Is ghi in?", "ghi" in alphabet)
print("Is Xyz in?", "Xyz" in alphabet)

print("Is f not in?", "f" not in alphabet)
print("Is F not in?", "F" not in alphabet)
print("Is 1 not in?", "1" not in alphabet)
print("Is ghi not in?", "ghi" not in alphabet)
print("Is Xyz not in?", "Xyz" not in alphabet)
