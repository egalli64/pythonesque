"""
0/1 knapsack

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
"""


def solution(knapsack, weights, values):
    table = [[0] * (knapsack + 1) for _ in range(0, len(weights) + 1)]

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if weights[i-1] <= j:
                table[i][j] = max(table[i-1][j], values[i-1] + table[i-1][j-weights[i-1]])
            else:
                table[i][j] = table[i-1][j]

    return table[-1][-1]

