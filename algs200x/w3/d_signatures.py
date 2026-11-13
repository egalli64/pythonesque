"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Collecting Signatures
Find the minimum number of points so that each passed segment has them in it.
"""


def solution(segments: list[tuple[int, int]]) -> list[int]:
    segments.sort(key=lambda item: item[1])

    results = [segments[0][1]]
    for segment in segments:
        if segment[0] > results[-1]:
            results.append(segment[1])

    return results
