"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

The Relative Immutability of Tuples - a tuple is an immutable container (but the content can change)
"""
t1 = (1, 2, [30, 40])
print("a tuple:", t1)
t2 = (1, 2, [30, 40])
print("another tuple:", t2)
print(f"different identity ({id(t1) is not id(t2)}), but same content ({t1 == t2})")

print("last item in the tuple is mutable, and has id", id(t1[-1]))
t1[-1].append(99)
print("I can change it (not changing its id)", t1[-1], id(t1[-1]))

print("sure enough, now the two tuples are different:", t1 != t2)
