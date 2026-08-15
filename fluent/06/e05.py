"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

List copy by built-in constructor
"""
l1 = [3, [55, 44], (7, 8, 9)]
print("a list", l1)

l2 = list(l1)
print(f"another list by copy-ctor: equal ({l1 == l2}) but not the same object ({id(l1) != id(l2)})")

l3 = l1[:]
print(f"same by [:], equal ({l1 == l3}) but not the same object ({id(l1) != id(l3)})")
