"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 1 - Generators, iterators, and closures
 4. More about list comprehensions
"""
a_list_1 = []

for ex in range(6):
    a_list_1.append(10**ex)

a_list_2 = [10**ex for ex in range(6)]

print(a_list_1)
print(a_list_2)

b_list_1 = []

for x in range(10):
    b_list_1.append(1 if x % 2 == 0 else 0)

b_list_2 = [1 if x % 2 == 0 else 0 for x in range(10)]

print(b_list_1)
print(b_list_2)

a_generator = (10**ex for ex in range(6))
for x in a_generator:
    print(x, end=" ")
print()

b_generator = (1 if x % 2 == 0 else 0 for x in range(10))
for x in b_generator:
    print(x, end=" ")
print()
