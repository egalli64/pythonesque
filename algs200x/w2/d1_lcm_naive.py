"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Least Common Multiple
Naive
"""


def lcm_naive(a: int, b: int) -> int:
    """
    Try all the values between the largest parameter and their product.
    """
    for tentative in range(max(a, b), a * b):
        if tentative % a == 0 and tentative % b == 0:
            return tentative
    return a * b
