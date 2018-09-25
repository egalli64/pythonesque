"""
Partitioning Souvenirs

taken from:
https://github.com/sraaphorst/data_structures_and_algorithms/blob/master/course_1_algorithmic_toolbox/week6_dynamic_programming2/2_partitioning_souvenirs/partition3.py
By Sebastian Raaphorst, 2018.

Manny egalli64@gmail.com
"""


def solution(items):
    third, module = divmod(sum(items), 3)
    if len(items) < 3 or module or max(items) > third:
        return False

    xy_len = third + 1
    z_len = len(items) + 1
    T = [[([False] * z_len)[:] for _ in range(xy_len)] for _ in range(xy_len)]
    T[0][0][0] = True

    for z in range(1, z_len):
        cur = items[z - 1]
        for x in range(xy_len):
            x_left = x - cur
            for y in range(xy_len):
                y_left = y - cur

                if x == 0 and y == 0:
                    T[0][0][z] = True
                elif cur == x and True in [T[i][y][z-1] for i in range(xy_len)]:
                    T[x][y][z] = True
                elif cur == y and True in [T[x][i][z-1] for i in range(xy_len)]:
                    T[x][y][z] = True
                elif T[x][y][z-1]:
                    T[x][y][z] = True
                elif x_left > 0 and T[x_left][y][z-1]:
                    T[x][y][z] = True
                elif y_left > 0 and T[x][y_left][z-1]:
                    T[x][y][z] = True

    return T[-1][-1][-1]


if __name__ == '__main__':
    while True:
        input()  # discard header

        items = [x for x in map(int, input().split())]
        print(solution(items))
        input()  # discard tail
