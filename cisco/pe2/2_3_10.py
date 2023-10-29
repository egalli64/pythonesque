"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 3 – String Methods /3
"""
# 10 The isupper() method
s10a = 'Moooo'
print(f"Is >{s10a}< upper-only?", s10a.isupper())

s10b = 'MOOOO'
print(f"Is >{s10b}< upper-only?", s10b.isupper())

# 11 The join() method
s11s = ["omicron", "pi", "rho"]
print(f"Joining {s11s} with a comma as separator:", ",".join(s11s))

# 12 The lower() method
s12a = 'SiGmA=60'
print(f">{s12a}< to lower is:", s12a.lower())

# 13 The lstrip() method
s13a = ' tau '
print(f"Left stripping >{s13a}< gives >" + s13a.lstrip() + "<")

s13b = 'www.cisco.com'
stripping = 'w.'
print(f"Left stripping >{s13b}< of >{stripping}< gives >" +
      s13b.lstrip(stripping) + "<")

# 14 The replace() method
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace(" juice", ""))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# 15 The rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# 16 The rstrip() method
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
