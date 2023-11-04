"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 1 - Generators, iterators, and closures
 5. The lambda function
 6. How to use lambdas and what for?
 7. Lambdas and the map() function
 8. Lambdas and the filter() function
 9. A brief look at closures
"""
two = lambda: 2
square = lambda x: x * x
power = lambda x, y: x**y

print("*** Using lambdas as plain functions")
for a in range(-2, 3):
    print(f"{a}: squared is {square(a)}, elevated to {two()} is {power(a, two())}")


print("*** Passing function vs passing lambda to an HOF")


def print_function(args, fun):
    for x in args:
        print(f"{fun.__name__}({x}) = {fun(x)}", end=", ")
    print()


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
# alas, lambda are anonymous, but they are handy
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

print("*** Lambdas and map")

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2**x, list_1))
print("Working with", list_1, list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=" ")
print()

print("*** Lambdas and filter")

from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print("Five values picked randomly in [-10, 10]:", data)
print("Filter them to keep the even and positive values only", filtered)

print("*** Closures")


def make_closure(exp):
    return lambda x: x**exp


square = make_closure(2)
cube = make_closure(3)

for i in range(5):
    print(f"{i} squared is {square(i)} and cubed is {cube(i)}")
