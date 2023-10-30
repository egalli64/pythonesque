"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 3 – String Methods /4
"""
# 17 The split() method
s17a = 'phi       chi\npsi'
s17s = s17a.split()
print(f"Splitting >{s17a}< leads to {s17s}")
print("Compare it with listing the chars in the string:", list(s17a))
print(f"Back to a single string by join() >{' '.join(s17s)}< ")

# 18 The startswith() method
s18a = 'omega'
s18c1 = 'meg'
s18c2 = 'om'
print(f"'{s18a}' starts with '{s18c1}'?", s18a.startswith(s18c1))
print(f"'{s18a}' starts with '{s18c2}'?", s18a.startswith(s18c2))

# 19 The strip() method
s19 = '   aleph   '
print(f"Stripping '{s19}' leads to '{s19.strip()}'")

# 20 The swapcase() method
s20 = 'I know that I know nothing'
print(f"Swapping case on '{s20}' leads to '{s20.swapcase()}'")

# 21 The title() method
s21 = 'I know that I know nothing. Part 1.'
print(f"Title on '{s21}' leads to '{s21.title()}'")

# 22 The upper() method
s22 = 'I know that I know nothing. Part 2.'
print(f"Upper on '{s22}' leads to '{s22.upper()}'")
