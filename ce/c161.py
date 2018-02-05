"""
Game of Life
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-game-of-life.html
      https://www.codeeval.com/open_challenges/161/
"""
import sys

STEPS = 10
ALIVE = '*'
DEAD = '.'


def local_population(matrix, i, j):
    result = 0
    for row in [i-1, i, i+1]:
        for col in [j-1, j, j+1]:
            if 0 <= row < len(matrix) and 0 <= col < len(matrix) \
                    and not (row == i and col == j) \
                    and matrix[row][col] == ALIVE:
                result += 1
    return result


def next_iteration(matrix):
    next_step = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            count = local_population(matrix, i, j)
            if matrix[i][j] == ALIVE:
                row.append(ALIVE if 1 < count < 4 else DEAD)
            else:
                row.append(ALIVE if count == 3 else DEAD)
        next_step.append(row)
    return next_step


def solution(data):
    step = [list(row) for row in data.rstrip().split('\n')]

    for i in range(STEPS):
        step = next_iteration(step)

    result = []
    for row in step:
        result.append(''.join([c for c in row]))
    return '\n'.join(result) + '\n'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'r')
        print(solution(file.read()))
        file.close()
    else:
        print('Data filename expected as argument!')
