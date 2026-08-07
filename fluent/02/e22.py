"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Arrays - based on C arrays
"""
from array import array
from random import random, seed

ARRAY_SIZE = 10 ** 5

# for output consistency
seed(10)

# use a genexp as iterable source for the float array
generator = (random() for i in range(ARRAY_SIZE))
# an array of double-precision floats (typecode "d")
a_float_array = array("d", generator)
print("Last element in the float array is:", a_float_array[-1])

# dump the array to file
with open('floats.tmp', 'wb') as fp:
    a_float_array.tofile(fp)

# load an array from file
cloned_array = array('d')
with open('floats.tmp', 'rb') as fp:
    cloned_array.fromfile(fp, ARRAY_SIZE)
print("Last element in the cloned array is:", cloned_array[-1])

print("The two arrays are the same:", a_float_array == cloned_array)
