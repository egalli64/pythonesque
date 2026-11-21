"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Organizing a Lottery
Given a list of segments and a list of points, say how many hits on the segments has each point
Naive
"""


def solution(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    results = []

    for point in points:
        result = 0
        for segment in segments:
            if segment[0] <= point <= segment[1]:
                result += 1
        results.append(result)

    return results
