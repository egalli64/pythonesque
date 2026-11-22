"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Finding the Closest Pair of Points
https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
Subhash Suri, UC Santa Barbara: http://www.cs.ucsb.edu/~suri/cs235/ClosestPair.pdf
Given n points on a plane, find the smallest distance between a pair of two (different) points.
Naive approach
"""
import math


def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def solution(points: list[tuple[int, int]]) -> float:
    size = len(points)
    if size < 2:
        return 0.0

    result = float('inf')
    for i in range(size - 1):
        for j in range(i + 1, size):
            result = min(result, distance(points[i], points[j]))
    return result
