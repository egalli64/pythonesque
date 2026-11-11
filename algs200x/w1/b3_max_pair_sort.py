"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w1

Week 1 - Maximum Pairwise Product
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
"""


def max_pair(values: list[int]) -> int:
    """
    Select the two largest numbers, save a lot of useless work.

    Raise AssertionError when precondition fails
    """
    assert len(values) > 1
    values.sort(reverse=True)

    return values[0] * values[1]
