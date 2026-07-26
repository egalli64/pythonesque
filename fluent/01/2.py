"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/vector2d.doctest
My playground: https://github.com/egalli64/pythonesque/ fluent folder

How Special Methods Are Used
"""
from vector2d import Vector

v1 = Vector(2, 4)
print("v1 is", v1)

v2 = Vector(2, 1)
print("v2 is", v2)

v12 = v1 + v2
print("v12 is", v12)

v = Vector(3, 4)
print(f"v is {v}, its abs is", abs(v))
v3 = v * 3
print("Triple of v is", v3)
print("And its abs is", abs(v3))
