"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w1

Week 1 - Maximum Pairwise Product
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
"""


def max_pair(values: list[int]) -> int:
    """
    Naive Algorithm

    Raise AssertionError when precondition fails
    """
    n = len(values)
    assert n > 1

    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            result = max(result, values[i] * values[j])

    return result
