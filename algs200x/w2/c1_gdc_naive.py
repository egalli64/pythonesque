"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Greater Common Divisor
Naive
"""


def gcd_naive(a: int, b: int) -> int:
    """
    Loop on all the integers up to the smallest parameter.
    If the current value is a divisor for both parameters, it is a good candidate.
    """
    result = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > result:
                result = d

    return result
