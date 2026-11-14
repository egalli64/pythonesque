"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Check if a sequence contains a majority element.
By Counter dictionary
"""
from collections import Counter


def solution(data: list[int]):
    return Counter(data).most_common(1)[0][1] > len(data) // 2
