"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Dictionary Views
"""
a_dict = dict(a=10, b=20, c=30)
print("A dict:", a_dict)

print("its keys:", a_dict.keys())
print("its items:", a_dict.items())

values = a_dict.values()
print(f"its {len(values)} values:", values)
print("from dict values to list:", list(values))

print("the reversed values:")
for x in reversed(values):
    print("\t", x)

try:
    # can't do that
    values[0]
except TypeError as e:
    print(f"{e!r}")

# a view is a dynamic proxy
a_dict['z'] = 99
print("A view sees the change in the original mapping:", values)
