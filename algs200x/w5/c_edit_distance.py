"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Computing the Edit Distance Between Two Strings
"""


def solution_dp(lhs: str, rhs: str) -> int:
    table = [[x for x in range(len(rhs) + 1)]]
    for k in range(1, len(lhs) + 1):
        table.append([k] + [0] * len(rhs))

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if lhs[i - 1] == rhs[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1

    return table[-1][-1]
