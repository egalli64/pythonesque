"""
Maximizing the Value of an Arithmetic Expression

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2
"""
CALCULATOR = {'*': lambda a, b: a*b, '+': lambda a, b: a+b, '-': lambda a, b: a-b}


def min_max(tab_min, tab_max, operations, i, j):
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


def solution(values, operations):
    n = len(values)

    tab_min = [[0 for _ in range(n)] for _ in range(n)]
    tab_max = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        tab_max[x][x] = tab_min[x][x] = values[x]

    for k in range(1, n):
        for i in range(n-k):
            min_max(tab_min, tab_max, operations, i, i+k)

    return tab_max[0][-1]


if __name__ == '__main__':
    line = input()
    lhs = [int(x) for x in line[::2]]
    rhs = [x for x in line[1::2]]

    print(solution(lhs, rhs))
