"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Tuples as Immutable Lists
"""
# Figure 2-4. the references held by the tuple will always point to the same objects
a = (10, 'alpha', [1, 2])
print("a is:", a, id(a))
b = (10, 'alpha', [1, 2])
print("b is:", b, id(b))
print("a == b?", a == b)  # True

b[-1].append(99)
print("a == b:", a == b)  # False

# an object is hashable if its value cannot change
c = (10, 'alpha', (1, 2))
try:
    hash(c)
    print("c is hashable")
except TypeError as ex:
    print("hash() raise a TypeError for", ex)
