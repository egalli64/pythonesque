"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Money Change Again
The greedy approach doesn't work for any denomination, find a different approach
Recursive approach
"""
DENOMINATIONS = [1, 3, 4]


def solution(target: int):
    if target == 0:
        return 0

    result = target  # assuming 1 is among the available denominations
    for coin in DENOMINATIONS:
        if target >= coin:
            tentative = solution(target - coin) + 1
            result = min(result, tentative)

    return result
