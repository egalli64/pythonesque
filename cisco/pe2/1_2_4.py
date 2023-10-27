"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 2 – Selected Python modules (math, random, platform)
Randomness
"""
import random as r

# always the same sequence of random numbers is generated, based on the passed seed
r.seed(0)

print("five random numbers in [0.0 .. 1.0): ", end=' ')
for i in range(5):
    print(r.random(), end=' ')
print()

print("ten random numbers in [0 .. 3): ", end=' ')
for i in range(10):
    print(r.randrange(3), end=' ')
print()

print("ten random numbers in [6 .. 10): ", end=' ')
for i in range(10):
    print(r.randrange(6, 10), end=' ')
print()

print("ten even random numbers in [2 .. 9): ", end=' ')
for i in range(10):
    print(r.randrange(2, 9, 2), end=' ')
print()

print("ten random numbers in [3 .. 6]: ", end=' ')
for i in range(10):
    print(r.randint(3, 6), end=' ')
print()

# choose numbers from a sequence
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Chosing from {values}")

print(" a single value:", r.choice(values))
print(" a sample of 5 elements", r.sample(values, 5))