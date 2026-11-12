"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing Revenue in Online Ad Placement
Given two sequences, partition them into n pairs, to maximize their sum
"""


def solution(profits: list[int], clicks: list[int]) -> int:
    profits.sort()
    clicks.sort()

    result = 0
    for profit, click in zip(profits, clicks):
        result += profit * click
    return result
