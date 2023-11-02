"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 10. LAB Triangle
"""
import math

import importlib
p = importlib.import_module("3_4_9")


class Triangle:
    def __init__(self, x1, x2, x3):
        self._xs = [x1, x2, x3]

    def perimeter(self):
        result = 0
        for i in range(3):
            result += self._xs[i].distance_from_point(self._xs[(i + 1) % 3])
        return result


triangle = Triangle(p.Point(0, 0), p.Point(1, 0), p.Point(0, 1))
print(triangle.perimeter())
