"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/vector2d.py
My playground: https://github.com/egalli64/pythonesque/ fluent folder

How Special Methods Are Used
"""
import math
from typing import override


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @override
    def __repr__(self):
        # notice the !r, use repr for x and y attributes
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        # Pythagoras to get the vector magnitude
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
