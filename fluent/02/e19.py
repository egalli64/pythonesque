"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Augmented Assignment with Sequences

+= makes use of __iadd__, in-place add dunder method
or __add__ as fallback -> not in-place, generates a new object
"""
# mutable seqs should implement __iadd__ and __imul__
a_list = [1, 2, 3]
print(id(a_list), a_list)

a_list *= 2
print(id(a_list), a_list)

# mutable seqs can't implement __iadd__ and __imul__
a_tuple = (1, 2, 3)
print(id(a_tuple), a_tuple)

a_tuple *= 2
print(id(a_tuple), a_tuple)
