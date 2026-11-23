"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Longest Common Subsequence of Three Sequences
"""


def solution(a: list[int], b: list[int], c: list[int]) -> int:
    cube = [[[0] * (len(b) + 1) for _ in range(len(a) + 1)] for _ in range(len(c) + 1)]

    for i in range(1, len(cube)):
        for j in range(1, len(cube[0])):
            for k in range(1, len(cube[0][0])):
                if a[j - 1] == b[k - 1] == c[i - 1]:
                    cube[i][j][k] = cube[i - 1][j - 1][k - 1] + 1
                else:
                    cube[i][j][k] = max(cube[i - 1][j][k], cube[i][j - 1][k], cube[i][j][k - 1])

    return cube[-1][-1][-1]
