"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Sharing Function Parameters - A function may change any mutable object it receives
"""


def f(a, b):
    print(f"in f, a is {a} ({id(a)})")
    a += b
    print(f"in f, now a is {a} ({id(a)})")
    return a


# ints are immutable
x = 1
y = 2
print(f"x is {x} ({id(x)}) and y is {y} ({id(y)})")
# being immutable, no change in x
print(f"the function returns {f(x, y)}, x is {x}, y is {y}")

# lists are mutable
l1 = [1, 2]
l2 = [3, 4]
# being mutable, l1 changes
print(f"l1 is {l1} ({id(l1)}) and l2 is {l2} ({id(l2)})")
print(f"the function returns {f(l1, l2)}, l1 is {l1}, l2 is {l2}")

# tuples are immutable
t1 = (10, 20)
t2 = (30, 40)
print(f"t1 is {t1} ({id(t1)}) and t2 is {t2} ({id(t2)})")
print(f"the function returns {f(t1, t2)}, t1 is {t1}, t2 is {t2}")
