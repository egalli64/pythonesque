"""
Extra exercise: 2-partition problem
https://github.com/egalli64/pythonesque folder algs200x/w6
"""


def solution(values: list[int]) -> int:
    total = sum(values)
    if total % 2:
        return False

    half = total // 2
    size = len(values) + 1
    table = [[False] * size for _ in range(half + 1)]

    for i in range(1, half + 1):
        for j in range(1, size):
            if values[j - 1] == i or table[i][j - 1]:
                table[i][j] = True
            else:
                ii = i - values[j - 1]
                if ii > 0 and table[ii][j - 1]:
                    table[i][j] = True

    return table[-1][-1]
