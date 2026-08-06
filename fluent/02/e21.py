"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

list.sort Versus the sorted Built-In
"""
fruits = ["grape", "raspberry", "apple", "banana"]
print(fruits)
fruits.sort()
print("in-place sort:", fruits)

fruits = sorted(fruits, reverse=True)
print("built-in reversed:", fruits)
print("built-in by len (stable):", sorted(fruits, key=len))
print("built-in reversed by len:", sorted(fruits, key=len, reverse=True))
