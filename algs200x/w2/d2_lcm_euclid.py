"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Least Common Multiple
Euclid based
"""
from math import gcd


def lcm(a: int, b: int) -> int:
    return 0 if a == 0 or b == 0 else (a * b) // gcd(a, b)
