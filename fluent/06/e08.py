"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Beware of cyclic references
"""
from copy import deepcopy

a = [10, 20]
print("a:", a)

# a list with a reference to another list
b = [a, 30]
print("b:", b)

# a cyclic reference
a += b
print("a += b:", a)

# a cyclic reference w/ deepcopy
c = deepcopy(a)
print("c:", c)
