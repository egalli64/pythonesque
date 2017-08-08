"""
CodeEval Minesweeper
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/79/
"""
import sys


def solution(rows, cols, data):
    board = []
    for i in range(rows):
        board.append(data[i*cols:(i+1)*cols])

    result = []
    for i in range(rows):
        line = []
        for j in range(cols):
            if board[i][j] == '*':
                line.append('*')
                continue

            up = i > 0
            down = i < rows - 1
            left = j > 0
            right = j < cols - 1

            count = 0
            if up:
                if left and board[i-1][j-1] == '*':
                    count += 1
                if board[i-1][j] == '*':
                    count += 1
                if right and board[i-1][j+1] == '*':
                    count += 1

            if left and board[i][j-1] == '*':
                count += 1
            if right and board[i][j+1] == '*':
                count += 1

            if down:
                if left and board[i+1][j-1] == '*':
                    count += 1
                if board[i+1][j] == '*':
                    count += 1
                if right and board[i+1][j+1] == '*':
                    count += 1

            line.append(str(count))
        result.append(line)

    return ''.join([''.join(x) for x in result])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.split(';')
                y, x = map(int, lhs.split(','))
                print(solution(y, x, rhs.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
