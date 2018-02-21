"""
Longest Common Subsequence of Two Sequences

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/longest-common-subsequence-of-two.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""


def solution_dp(lhs, rhs):
    table = [[0] * (len(rhs) + 1)]
    for _ in range(1, len(lhs) + 1):
        table.append([0] * (len(rhs) + 1))

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if lhs[i - 1] == rhs[j - 1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]


if __name__ == '__main__':
    input()  # size discarded
    a = [int(x) for x in input().split()]
    input()  # size discarded
    b = [int(x) for x in input().split()]
    print(solution_dp(a, b))
