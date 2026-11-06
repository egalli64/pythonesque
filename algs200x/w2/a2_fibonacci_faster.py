"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - A faster Fibonacci calculator
"""


def calc_fib(n: int):
    if n <= 1:
        return n

    results = [1, 1]
    for _ in range(n - 2):
        minor = results[0]
        results[0] = results[1]
        results[1] = minor + results[0]

    return results[-1]
