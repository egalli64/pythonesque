"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 6 - Dynamic Programming /2: Partitioning Souvenirs
https://github.com/sraaphorst/data_structures_and_algorithms/blob/master/course_1_algorithmic_toolbox/week6_dynamic_programming2/2_partitioning_souvenirs/partition3.py
By Sebastian Raaphorst, 2018.
"""


def solution(items: list[int]) -> bool:
    third, module = divmod(sum(items), 3)
    if len(items) < 3 or module or max(items) > third:
        return False

    xy_len = third + 1
    z_len = len(items) + 1
    table = [[([False] * z_len)[:] for _ in range(xy_len)] for _ in range(xy_len)]
    table[0][0][0] = True

    for z in range(1, z_len):
        cur = items[z - 1]
        for x in range(xy_len):
            x_left = x - cur
            for y in range(xy_len):
                y_left = y - cur

                if x == 0 and y == 0:
                    table[0][0][z] = True
                elif cur == x and True in [table[i][y][z - 1] for i in range(xy_len)]:
                    table[x][y][z] = True
                elif cur == y and True in [table[x][i][z - 1] for i in range(xy_len)]:
                    table[x][y][z] = True
                elif table[x][y][z - 1]:
                    table[x][y][z] = True
                elif x_left > 0 and table[x_left][y][z - 1]:
                    table[x][y][z] = True
                elif y_left > 0 and table[x][y_left][z - 1]:
                    table[x][y][z] = True

    return table[-1][-1][-1]
