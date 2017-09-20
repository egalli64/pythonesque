"""
CodeEval Query Board
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/09/codeeval-query-board.html
      https://www.codeeval.com/open_challenges/87/
"""
import sys

ID_2_NAME = {'SetRow': 'set_row', 'SetCol': 'set_col', 'QueryRow': 'query_row', 'QueryCol': 'query_col'}


class Board:
    def __init__(self, size=256):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def set_row(self, i, value):
        for j in range(self.size):
            self.board[i][j] = value

    def set_col(self, j, value):
        for i in range(self.size):
            self.board[i][j] = value

    def query_row(self, i):
        return sum(self.board[i])

    def query_col(self, j):
        result = 0
        for i in range(self.size):
            result += self.board[i][j]
        return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            board = Board()
            for line in file:
                command, *params = line.split()
                res = getattr(board, ID_2_NAME[command])(*[int(p) for p in params])
                if res is not None:
                    print(res)
    else:
        print('Data filename expected as argument!')
