"""
Maximum Amount of Gold

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/other-dynamic-programming-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2
"""


def solution(knapsack, bars):
    table = [[0] * (knapsack + 1) for _ in range(0, len(bars) + 1)]

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if bars[i-1] <= j:
                table[i][j] = max(table[i-1][j], bars[i-1] + table[i-1][j-bars[i-1]])
            else:
                table[i][j] = table[i-1][j]

    return table[-1][-1]


if __name__ == '__main__':
    a = int(input().split()[0])
    b = [x for x in map(int, input().split())]

    print(solution(a, b))
