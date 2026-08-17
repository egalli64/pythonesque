"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

del and Garbage Collection
"""
a = [1, 2]
print("create a list and bind it to variable a:", a)

b = a
print("bind b to the same list object:", b)

del a
print("after del on a, b is still there (doh!):", b)

try:
    print(a)
except NameError as e:
    print(f"Sure enough, a is no more there: {e!r}")

print("the list id is", id(b))
b = []
print(f"now the list id is {id(b)} and the old list could be garbage collected")
