"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Unpacking Sequences and Iterables
"""
lax_coordinates = (33.9425, -118.408056)

# unpacking by parallel assignment
latitude, longitude = lax_coordinates
print("LAX latitude: ", latitude)
print("LAX longitude: ", longitude)

# unpacking for swapping variable values
a = 42
b = 7
print(a, b)
a, b = b, a
print(a, b)

# unpacking arguments
t = (20, 8)
quotient, remainder = divmod(*t)
print(f"divmod of {t} gives {quotient} and {remainder}")

# using underscore to imply that unpacked values are not used
_, remainder = divmod(*t)
print("The remainder is", remainder)
