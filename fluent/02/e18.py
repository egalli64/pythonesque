"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Building Lists of Lists
"""
# Example 2-14 - a tic-tac-toe board
board = [["_"] * 3 for i in range(3)]
print(board)

# Place a mark in row 1, column 2
board[1][2] = "X"
print("Good", board)

# Example 2-15 - a mistake
weird_board = [['_'] * 3] * 3
print(weird_board)

# All rows are aliases of the same object!
weird_board[1][2] = "O"
print("Bug!", weird_board)

# 2.14 rewritten without listcomp
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
board[2][0] = 'X'
print("Good", board)

# 2.15 rewritten without listcomp
board = []
row = ['_'] * 3
for i in range(3):
    board.append(row)
print(board)
board[2][0] = 'X'
print("Bug!", board)
