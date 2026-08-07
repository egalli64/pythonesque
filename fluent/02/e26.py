"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Mixed bag lists
"""
a_list = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
print("a dangerous list:", a_list)

try:
    # can't sort an iterable of incompatible types
    sorted(a_list)
except TypeError as e:
    print(repr(e))
