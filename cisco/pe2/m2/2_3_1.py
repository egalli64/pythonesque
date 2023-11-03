"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 3 – String Methods
"""
# 1 The capitalize() method
s1a = 'aBcD'
print(f"{s1a} capitalized is", s1a.capitalize())
s1b = "δαβγ"
print(f"{s1b} capitalized is", s1b.capitalize())

# 2 The center() method
s2a = 'alpha'
print(f'{s2a} centered 10 is [' + s2a.center(10) + ']')
s2b = 'beta'
print(f'{s2b} centered 2 is [' + s2b.center(2) + ']')
s2c = 'gamma'
print(f'{s2c} centered 20 with "*" is [' + s2c.center(20, '*') + ']')

# 3 The endswith() method
s3a = 'epsilon'
s3b = 'on'
if s3a.endswith(s3b):
    print(f"As expected >{s3a}< ends with >{s3b}<")
else:
    print("Unexpected!")

# 4 The find() method
s4a = 'eta'
s4b = 'ta'
s4c = 'x'
print(f"Find >{s4b}< in >{s4a}< gives", s4a.find(s4b))
print(f"Find >{s4c}< in >{s4a}< gives", s4a.find(s4c))

s4d = 'kappa'
s4e = 'a'
print(f"Find >{s4e}< in >{s4d}< gives", s4d.find(s4e))
print(f"Find >{s4e}< in >{s4d}< from 2 gives", s4d.find(s4e, 2))

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

print("Looking for 'the' in string:", the_text)
print("Found at", end=' ')
fnd = the_text.find('the')
while fnd != -1:
    print(fnd, end=' ')
    fnd = the_text.find('the', fnd + 1)
print()
