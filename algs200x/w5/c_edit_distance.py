"""
Computing the Edit Distance Between Two Strings

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/computing-edit-distance-between-two.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""


def solution_dp(lhs, rhs):
    table = [[x for x in range(len(rhs) + 1)]]
    for k in range(1, len(lhs) + 1):
        table.append([k] + [0] * len(rhs))

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if lhs[i - 1] == rhs[j - 1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1

    return table[-1][-1]


if __name__ == '__main__':
    a = input()
    b = input()
    print(solution_dp(a, b))
