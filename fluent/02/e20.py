"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A += Assignment Puzzler - Example 2-16. A riddle
"""
a_tuple = (1, 2, [30, 40])
try:
    a_tuple[2] += [50, 60]
except TypeError as e:
    print("TypeError detected:", e)
finally:
    print("Still, the assignment is performed!", a_tuple)

# if you really want to get this effect use extends on the list:
a_tuple = (1, 2, [30, 40])
a_tuple[2].extend([50, 60])
print("exception free behavior:", a_tuple)
