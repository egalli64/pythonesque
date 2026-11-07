"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Greater Common Divisor
Euclid
"""


def gcd_recursive(a: int, b: int) -> int:
    return a if b == 0 else gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
