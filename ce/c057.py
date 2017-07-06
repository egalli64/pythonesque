"""
CodeEval Spiral Printing
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/57/
"""
import sys


def solution(rows, cols, values):
    # push the values in matrix format
    matrix = []
    values = values.split()
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(values[i*cols + j])

    result = []

    left, top, bottom, right = 0, 0, rows, cols
    while left < right:
        # scan right
        for j in range(left, right):
            result.append(matrix[top][j])
        # top row consumed
        top += 1
        if top == bottom:
            break

        # scan down
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        # right row consumed
        right -= 1
        if right == left:
            break

        # scan left
        for j in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][j])
        # bottom row consumed
        bottom -= 1
        if top == bottom:
            break

        # scan up
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        # left row consumed
        left += 1

    return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                y, x, k = test.split(';')
                print(solution(int(y), int(x), k))
    else:
        print('Data filename expected as argument!')
