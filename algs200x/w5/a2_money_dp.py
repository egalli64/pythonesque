"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Money Change Again
The greedy approach doesn't work for any denomination, find a different approach
Dynamic Programming
"""
DENOMINATIONS = [1, 3, 4]


def solution(target: int) -> int:
    cache = [0] * (target + 1)

    for i in range(1, target + 1):
        cache[i] = cache[i - 1] + 1  # assuming DENOMINATIONS[0] == 1
        for coin in DENOMINATIONS[1:]:
            if coin <= i:
                other = cache[i - coin] + 1
                cache[i] = min(cache[i], other)

    return cache[-1]
