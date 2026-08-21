"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

functools.reduce on a lambda
"""
from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


print(factorial(5))
