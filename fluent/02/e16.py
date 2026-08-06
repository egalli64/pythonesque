"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Assigning to Slices
"""
a_list = list(range(10))
print(a_list)

# slice assignment to replace a section of a list
a_list[2:5] = [20, 30]
print(a_list)

# slice deletion
del a_list[5:7]
print(a_list)

# extended slice assignment, be careful on the len of the assigned seq
a_list[3::2] = [11, 22]
print(a_list)

# this won't work, rhs must be an iterable
try:
    a_list[2:5] = 100
    print(a_list)
except TypeError as e:
    print("Would fail:", e)
