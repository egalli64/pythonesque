"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Why Slices and Ranges Exclude the Last Item
"""
a_list = [10, 20, 30, 40, 50, 60]

print("A range of three:", *range(3))
print("A list slice of three:", a_list[:3])

print("Head of list:", a_list[:3])
print("Rest of list:", a_list[3:])
