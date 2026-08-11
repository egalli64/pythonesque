"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Set Operations on dict Views
"""
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)

print(f"given two dict, {d1} and {d2}, get the common keys.")
print("Easy, with intersection:", d1.keys() & d2.keys())

a_set = {'a', 'e', 'i'}
print(f"Is there any key from this set {a_set} in {d1}?")
print("Again, intersection:", d1.keys() & a_set)
print("If you need to use union, that's easy too:", d1.keys() | a_set)
