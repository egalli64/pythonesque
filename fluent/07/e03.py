"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Modern Replacements for map, filter, and reduce
"""
from functools import reduce
from operator import add
from e01 import factorial

# map() is a built-in, but it is not anymore the preferred approach
print("using map on factorial:", list[int](map(factorial, range(6))))
# considered more pythonic
print("same, by listcomp:", [factorial(n) for n in range(6)])

# using map and filter (both built-in) together
filtered_list = list[int](map(factorial, filter(lambda n: n % 2, range(6))))
print("using map and filter on factorial:", filtered_list)
print("same, by listcomp:", [factorial(n) for n in range(6) if n % 2])

# reduce is not anymore a built-in, the built-in sum, all, any, offer alternative reducing approaches
print("passing the operator add to the reduce HOF:", reduce(add, range(100)))
print("here the built-in sum() makes the same job easier:", sum(range(100)))
