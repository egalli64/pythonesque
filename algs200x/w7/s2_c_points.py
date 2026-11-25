"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Greedy Algorithms
Covering points by segments
You are given ten points on a line, [1, 2, 3, 5, 7, 9, 10, 11, 13, 15]
You would like to cover them with the least number of segments of length three.
"""
SIZE = 3


def solution(points: list[int]) -> int:
    result = 1
    current = points[0]

    for point in points:
        if current + SIZE < point:
            current = point
            result += 1
    return result


if __name__ == '__main__':
    print(solution([1, 2, 3, 5, 7, 9, 10, 11, 13, 15]))
