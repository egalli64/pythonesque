"""
2-partition problem

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/2-partition-problem.html
"""


def solution(values):
    total = sum(values)
    if total % 2:
        return False

    half = total // 2
    table = [[False] * (len(values) + 1) for _ in range(half + 1)]

    for i in range(1, half + 1):
        for j in range(1, len(values) + 1):
            if values[j-1] == i or table[i][j-1]:
                table[i][j] = True
            else:
                ii = i-values[j-1]
                if ii > 0 and table[ii][j-1]:
                    table[i][j] = True

    return table[-1][-1]
