"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Unpacking with * in Function Calls and Sequence Literals
"""


def fun(a, b, c, d, *rest):
    """A function that takes 4+ parameters"""
    return a, b, c, d, rest


print(fun(*[1, 2], 3, *range(4, 7)))
print(fun(1, 2, 3, 4))

# Using * when defining tuple, list, or set literals
a_tuple = *range(4), 4
print("A tuple:", a_tuple)

a_list = [*range(4), 4]
print("A list:", a_list)

a_set = {*range(4), 4, *(5, 6, 7)}
print("A set:", a_set)
