"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 3 – String Methods /2
"""
# 5 The isalnum() method
s5a = 'lambda30'
print(f"Is >{s5a}< alphanumeric-only?", s5a.isalnum())

s5b = 'lambda_30'
print(f"Is >{s5b}< alphanumeric-only?", s5b.isalnum())

s5c = ''
print(f"Is >{s5c}< alphanumeric-only?", s5c.isalnum())

s5d = '&Alpha;&beta;&Gamma;&delta;'
print(f"Is >{s5d}< alphanumeric-only?", s5d.isalnum())

# 6 The isalpha() method
s6a = 'Moooo'
print(f"Is >{s6a}< alpha-only?", s6a.isalpha())

s6b = 'Mu40'
print(f"Is >{s6b}< alpha-only?", s6b.isalpha())

# 7 The isdigit() method
s7a = '2023'
print(f"Is >{s7a}< digit-only?", s7a.isdigit())

s7b = 'Year2024'
print(f"Is >{s7b}< digit-only?", s7b.isdigit())

# 8 The islower() method
s8a = 'Moooo'
print(f"Is >{s8a}< lower-only?", s8a.islower())

s8b = 'moooo'
print(f"Is >{s8b}< lower-only?", s8b.islower())

# 9 The isspace() method
s9a = ' \n '
print(f"Is >{s9a}< space-only?", s9a.isspace())

s9b = 'mooo mooo mooo'
print(f"Is >{s9b}< space-only?", s9b.isspace())
