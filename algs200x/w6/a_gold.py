"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 6 - Dynamic Programming /2: Maximum Amount of Gold
Given the capacity and a list of bars, find the maximum weight that could be taken
"""


def solution(knapsack: int, bars: list[int]) -> int:
    table = [[0] * (knapsack + 1) for _ in range(0, len(bars) + 1)]

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if bars[i - 1] <= j:
                table[i][j] = max(table[i - 1][j], bars[i - 1] + table[i - 1][j - bars[i - 1]])
            else:
                table[i][j] = table[i - 1][j]

    return table[-1][-1]


if __name__ == '__main__':
    a = int(input().split()[0])
    b = [x for x in map(int, input().split())]

    print(solution(a, b))
