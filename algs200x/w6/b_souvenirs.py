"""
Partitioning Souvenirs

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/partitioning-souvenirs.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2 - 3-Partition problem
"""


def solution(values):
    total = sum(values)
    if len(values) < 3 or total % 3:
        return False
    third = total // 3
    table = [[0] * (len(values) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            ii = i - values[j - 1]
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]

    return True if table[-1][-1] == 2 else False


if __name__ == '__main__':
    while True:
        input()  # discard header

        items = [x for x in map(int, input().split())]
        print(solution(items))
        input()  # discard tail
