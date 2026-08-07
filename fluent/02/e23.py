"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Memory Views - inspired by NumPy array, used to share memory among data structures
"""
from array import array

# an array of bytes - typecode "B"
a_byte_array = array("B", range(6))
# a memory view of the array
a_memory_view = memoryview(a_byte_array)
# export the memory view to a list
a_list = a_memory_view.tolist()
print(a_list)

# cast - here just to change shape
m2 = a_memory_view.cast('B', [2, 3])
print(m2.tolist())
# another shape
m3 = a_memory_view.cast('B', [3, 2])
print(m3.tolist())

# the memory is shared!
m2[1, 1] = 22
m3[1, 1] = 33
print(a_byte_array)
