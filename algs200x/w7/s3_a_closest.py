"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Divide and Conquer
Closest Elements
Given an int list, compute the smallest absolute difference between two of its elements.
"""


def solution(values: list[int]) -> int:
    result = 10 ** 9  # ensure this could be assumed a good sentinel value
    values.sort()

    for i in range(len(values) - 1):
        result = min(result, values[i + 1] - values[i])
    return result


if __name__ == '__main__':
    print(solution([870, 695, 790, 170, 918, 932, 539, 802, 648, 362, 770, 884, 377, 424, 845]))
