"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Finding the Closest Pair of Points
https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
Subhash Suri, UC Santa Barbara: http://www.cs.ucsb.edu/~suri/cs235/ClosestPair.pdf
Given n points on a plane, find the smallest distance between a pair of two (different) points.
Divide and Conquer approach
"""
from f1_closest_naive import distance, solution as solution_naive


def closest_distance(points: list[tuple[int, int]]):
    size = len(points)
    if size <= 3:
        return solution_naive(points)

    lhs = points[:size // 2]
    rhs = points[size // 2:]

    left = closest_distance(lhs)
    right = closest_distance(rhs)
    result = min(left, right)
    if result == 0.0:
        return result

    median = (lhs[-1][0] + rhs[0][0]) / 2
    closers = []
    for i in range(len(lhs)):
        if abs(lhs[i][0] - median) < result:
            closers.append(lhs[i])
    for i in range(len(rhs)):
        if abs(rhs[i][0] - median) < result:
            closers.append(rhs[i])
    closers.sort(key=lambda p: p[1])

    for i in range(len(closers) - 1):
        for j in range(i + 1, min(i + 6, len(closers))):
            if abs(closers[i][1] - closers[j][1]) < result:
                result = min(result, distance(closers[i], closers[j]))
    return result


def solution(points: list[tuple[int, int]]) -> float:
    points.sort()
    return closest_distance(points)
