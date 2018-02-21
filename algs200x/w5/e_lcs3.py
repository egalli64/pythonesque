"""
Longest Common Subsequence of Three Sequences

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/longest-common-subsequence-of-three.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""


def solution_dp(a, b, c):
    cube = []
    for m in range(len(c) + 1):
        sheet = [[0] * (len(b) + 1)]
        for n in range(1, len(a) + 1):
            sheet.append([0] * (len(b) + 1))
        cube.append(sheet)

    for i in range(1, len(cube)):
        for j in range(1, len(cube[0])):
            for k in range(1, len(cube[0][0])):
                if a[j - 1] == b[k - 1] == c[i - 1]:
                    cube[i][j][k] = cube[i - 1][j - 1][k - 1] + 1
                else:
                    cube[i][j][k] = max(cube[i - 1][j][k], cube[i][j - 1][k], cube[i][j][k - 1])

    return cube[-1][-1][-1]


if __name__ == '__main__':
    input()  # size discarded
    v1 = [int(x) for x in input().split()]
    input()  # size discarded
    v2 = [int(x) for x in input().split()]
    input()  # size discarded
    v3 = [int(x) for x in input().split()]
    print(solution_dp(v1, v2, v3))
