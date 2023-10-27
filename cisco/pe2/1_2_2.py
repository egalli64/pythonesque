"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 2 – Selected Python modules (math, random, platform)
"""
import math

# each attribute in a module (or class, object)
for name in dir(math):
    print(name, end="\t")

# the list with all of them
print(dir(math))

print("Trigonometry")
print(f" sin: {math.sin(0)}, cos {math.cos(0)}, tan {math.tan(0)}")
print(f" arcsin: {math.asin(0)}, arccos {math.acos(1)}, arctan {math.atan(0)}")
print(f" pi: {math.pi}")
print(f" radians: {math.radians(90)}")
print(f" degrees: {math.degrees(math.pi / 2)}")

print("Exponentiation")
print(f" e: {math.e}")
print(f" e^x: {math.exp(3)}")
print(f" log: {math.log(20)}")

print("Other functions")
print(f" ceil: {math.ceil(41.52)}")
print(f" floor: {math.floor(42.12)}")
print(f" trunc: {math.trunc(42.92)}")
print(f" factorial: {math.factorial(5)}")
print(f" hypot: {math.hypot(3, 4)}")
