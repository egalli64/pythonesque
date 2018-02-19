"""
Finding the Closest Pair of Points

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      http://thisthread.blogspot.com/2018/02/the-closest-pair-of-points.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
      Subhash Suri, UC Santa Barbara: http://www.cs.ucsb.edu/~suri/cs235/ClosestPair.pdf
      week 4 - Divide and Conquer
"""
import math


def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def solution_naive(points):
    size = len(points)
    if size < 2:
        return 0.0

    result = float('inf')
    for i in range(size - 1):
        for j in range(i+1, size):
            result = min(result, distance(points[i], points[j]))
    return result


def closest_distance(points):
    size = len(points)
    if size < 4:
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


def solution_dac(points):
    points.sort()
    return closest_distance(points)


if __name__ == '__main__':
    items = []
    for _ in range(int(input())):
        items.append(tuple(map(int, input().split())))
    print(solution_dac(items))
