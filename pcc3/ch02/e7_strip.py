"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 2 - Strings - Strip
"""
name = "    Guido   "
print(f"_{name}_")
print(f"_{name.lstrip()}_")
print(f"_{name.rstrip()}_")
print(f"_{name.strip()}_")

# remove prefix/suffix
steak = "sirloin"
print(steak)
print(steak.removeprefix("sir"))
print(steak.removesuffix("loin"))
