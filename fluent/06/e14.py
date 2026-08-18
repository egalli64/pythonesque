"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Tricks Python Plays with Immutables
"""
# tuple behavior
t1 = (1, 2, 3)
t2 = tuple(t1)
print("copy ctor on a tuple is just a reference copy:", t2 is t1)

t3 = t1[:]
print("tuple full slice is just a reference copy too:", t3 is t1)

t4 = (1, 2, 3)
print("a new tuple, even if equal, could be a different object. Don't trust it:", t4 is t1)

# string behavior
s1 = "ABC"
s2 = "ABC"

print("for strings and ints interning is used to save memory. But don't trust it:", s1 is s2)
