"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing the Number of Prize Places in a Competition
Given the number of candies, generate the largest possible monotonic sequence adding up to that value
"""


def solution(candies: int) -> list[int]:
    assert candies > 0

    unassigned = candies
    results = []
    for i in range(1, candies):
        if unassigned - i <= i:
            results.append(unassigned)
            break
        else:
            results.append(i)
            unassigned -= i

    return results
