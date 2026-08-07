"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Memory Views - change format
"""
from array import array

a_list = [-2, -1, 0, 1, 2]
# typecode "h" is for signed integer
an_int_array = array("h", a_list)
print(f"int array has len {len(an_int_array)}, its third element is {an_int_array[2]}")
mv = memoryview(an_int_array)
print(f"int memory view has len {len(mv)}, its third element is {mv[2]}")

# a new memory view with byte format
mv_bytes = mv.cast("B")
print(f"byte memory view has len {len(mv_bytes)}, its fifth element was {mv_bytes[5]}", end=", ")

# change an element in the buffer, seen as a byte memory view
mv_bytes[5] = 4
print(f"and it is changed to {mv_bytes[5]}")
print("The original int array third element has changed to", an_int_array[2])
