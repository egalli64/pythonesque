"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

What Is Hashable - A container is hashable if it is immutable and all contained objects are also hashable
"""


def f(x):
    try:
        # try to generate the hash code for the given object
        hash(x)
        print(x, "is hashable")
    except TypeError as e:
        print(x, "is not hashable,", e)


a_hashable_tuple = (1, 2, (30, 40))
non_hashable_tuple = (1, 2, [30, 40])
another_hashable_tuple = (1, 2, frozenset([30, 40]))

f(a_hashable_tuple)
f(non_hashable_tuple)
f(another_hashable_tuple)
