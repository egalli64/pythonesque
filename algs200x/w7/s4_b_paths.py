"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Dynamic Programming
Number of Paths in a Grid
Given an n-dimensional grid:
- start at the bottom left cell. In one step, you are allowed to go either one cell up or one cell to the right.
- the goal is to compute the number of different paths from the bottom left cell to the top right cell.
"""


def solution(size):
    table = [[1 for _ in range(size)] for _ in range(size)]
    for i in range(1, size):
        for j in range(1, size):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[-1][-1]


if __name__ == '__main__':
    print(solution(5))
