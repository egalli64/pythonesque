"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 11. LAB Sudoku
 - Check if the sudoko solution passed is acceptable
"""


def is_good_block(block):
    """Check if all the values in [1..9] are in the passed block"""
    return sorted(block) == [x for x in range(1, 10)]


def check_rows(rows):
    for row in rows:
        if not is_good_block(row):
            return False
    return True


def check_columns(rows):
    for i in range(9):
        column = []
        for j in range(9):
            column.append(rows[i][j])
        if not is_good_block(column):
            return False
    return True


def check_squares(rows):
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(rows[y+i][x+j])
            if not is_good_block(square):
                return False
    return True


def is_good(sudoku):
    return len(sudoku) == 9 and check_rows(sudoku) and check_columns(sudoku) and check_squares(sudoku)


rows_1 = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 7, 2]
]

print(is_good(rows_1))  # True

rows_2 = [
    [1, 9, 5, 7, 4, 3, 8, 6, 2],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [2, 5, 4, 9, 3, 8, 6, 7, 1]
]

print(is_good(rows_2))  # False

rows_3 = [
    [1, 9, 5, 7, 4, 3, 8, 6, 2]
]

print(is_good(rows_3))  # False

rows_4 = [
    [1, 9, 5, 7, 4, 3, 8, 6],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [2, 5, 4, 9, 3, 8, 6, 7, 1]
]

print(is_good(rows_4))  # False
