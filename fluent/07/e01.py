"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Treating a Function Like an Object
"""


def factorial(n):
    """a recursive function returning n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# a function could be called
print("42! is", factorial(42))
# a function has fields
print("the factorial function docstring is:", factorial.__doc__)
# a function is an instance of the function class
print("factorial is an instance of the function class:", type(factorial))

# a function is an object, and is used as any other object
fact = factorial
print("calling the factorial function through its fact alias:", fact(5))
# function can be passed to another function
fact_it = map(factorial, range(11))
print("a map object returned by mapping factorial to a range", fact_it)
print("materializing the lazy iterator in a list:", list(fact_it))
# Python is not a pure FP language, often alternative approaches are preferred
print("Same result, in a more pythonic way:", [factorial(n) for n in range(11)])
