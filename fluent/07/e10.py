"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

functools.reduce on operator.mul
"""
from functools import reduce
from operator import mul


def factorial(n: int):
    return reduce(mul, range(1, n + 1))


print(factorial(5))
