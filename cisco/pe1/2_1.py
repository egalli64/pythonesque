"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 2 Section 1 "Hello, World!"
"""
# escape for newline: \n
print("The itsy bitsy spider\nclimbed up the waterspout.")
# no-arg print, to print just a newline
print()
print("A single backslash: \\")

# multiple arguments
print("The itsy bitsy spider", "climbed up", "the waterspout.")

# positional vs keyword arguments, by default end is \n
print("My name is", "Python.", end=" ")
print("Monty Python.")
# by default sep is a single blank
print("My", "name", "is", "Monty", "Python.", sep="-")

# * as string multiplier
print("Hello" * 3)
