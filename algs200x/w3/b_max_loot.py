"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing the Value of a Loot
Find the most valuable combination of fractionable items
"""


def solution(capacity: int, items: list[tuple[int, int]]) -> float:
    result = 0.0
    loot = sorted(items, key=lambda item: item[0] / item[1])

    available = capacity
    while loot and available > 0:
        current = loot[-1][1] if loot[-1][1] < available else available
        result += loot[-1][0] / loot[-1][1] * current
        available -= current
        loot.pop()

    return result
