"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 4 - Working With Lists - Tuples

A tuple is an immutable list
"""
dimensions = (200, 50)
print(dimensions[0], dimensions[1], dimensions)

try:
    dimensions[0] = 42
except TypeError:
    print("Can't change a tuple")

# can loop on tuple
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Reassigned tuple:", dimensions)
