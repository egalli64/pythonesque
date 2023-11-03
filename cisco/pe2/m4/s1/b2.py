"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 1 - Generators, iterators, and closures
 2. The yield statement
 3. How to build a generator
"""


def powers_of_2(n):
    """yield is used to describe the behavior of a generator"""
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(11):
    print(v, end=" ")
print()

# list() could be used to convert a generator in a list
t = list(powers_of_2(11))
print(t)

# the operator in could be used against a generator
for i in range(20):
    if i in powers_of_2(4):
        print(i)


def fibonacci(n):
    """Fibonacci generator"""
    p1 = p2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p1 + p2
            p2, p1 = p1, n
            yield n


fibs = list(fibonacci(10))
print("Fibonacci of [0..10)", fibs)
