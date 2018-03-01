"""
Number of Paths in a Grid

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - dynamic programming

Given a 5x5 grid.
You start at the bottom left cell. In one step, you are allowed to go either one cell up or one cell to the right.
Your goal is to compute the number of different paths from the bottom left cell to the top right cell.
"""


def solution(size):
    table = [[1 for _ in range(size)] for _ in range(size)]
    for i in range(1, size):
        for j in range(1, size):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[-1][-1]


if __name__ == '__main__':
    print(solution(5))
