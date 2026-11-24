"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w6

Week 6 - Dynamic Programming /2: Maximizing the Value of an Arithmetic Expression
Given a list of integer and a list of intermixed arithmetic operation, maximize the expression result
"""
CALCULATOR = {'*': lambda a, b: a * b, '+': lambda a, b: a + b, '-': lambda a, b: a - b}


def min_max(tab_min: list, tab_max: list, operations: list, i: int, j: int) -> None:
    lowest = float('inf')
    highest = float('-inf')
    for k in range(i, j):
        op = CALCULATOR[operations[k]]

        a = op(tab_max[i][k], tab_max[k + 1][j])
        b = op(tab_max[i][k], tab_min[k + 1][j])
        c = op(tab_min[i][k], tab_max[k + 1][j])
        d = op(tab_min[i][k], tab_min[k + 1][j])

        lowest = min(lowest, a, b, c, d)
        highest = max(highest, a, b, c, d)

    tab_min[i][j] = lowest
    tab_max[i][j] = highest


def solution(values: list[int], operations: list[str]) -> int:
    n = len(values)

    tab_min = [[0 for _ in range(n)] for _ in range(n)]
    tab_max = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        tab_max[x][x] = tab_min[x][x] = values[x]

    for k in range(1, n):
        for i in range(n - k):
            min_max(tab_min, tab_max, operations, i, i + k)

    return tab_max[0][-1]
