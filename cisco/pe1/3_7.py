"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 7 – Lists in advanced applications
"""
# 3.7.1 Lists in lists
# List comprehensions
EMPTY = "__"
WHITE_PAWN = "W_"
BLACK_PAWN = "W_"
WHITE_ROOK = "WR"
BLACK_ROOK = "BR"

row = [WHITE_PAWN for i in range(8)]
print("A row:", row)

# Example #1
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)

# Example #2
twos = [2 ** i for i in range(8)]
print("Powers of 2:", twos)

# Example #3
odds = [x for x in squares if x % 2 != 0]
print("Odd squares:", odds)

# 3.7.2 Two-dimensional arrays
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print("Empty board", board)

# as nested list comprehension
board = [[EMPTY for i in range(8)] for j in range(8)]
print("Empty board", board)

board[0][0] = BLACK_ROOK
board[0][7] = BLACK_ROOK
board[7][0] = WHITE_ROOK
board[7][7] = WHITE_ROOK
print("Rooks on board", board)

# 3.7.3 Multidimensional nature of lists: advanced applications
temps = [[0.0 for h in range(24)] for d in range(31)]

# noon average calculator
total = 0.0
for day in temps:
    total += day[11]
average = total / 31
print("Average temperature at noon:", average)

# highest detector
highest = temps[0][0]
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("The highest temperature was:", highest)

# hot days checker
hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
print(hot_days, "days were hot")

# Hotel with 3 buildings, 15 floors for each building, 20 rooms for each floor
# Each element keep information on the room status, free or occupied (True)
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# checkin and checkout
rooms[2][14][13] = True
rooms[0][4][1] = False

# Look for vacancies on the 15th floor of the third building (for-range)
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print("Vacancies in 2 - 14:", vacancy)

# (for-each)
vacancy = 0
for room in rooms[2][14]:
    if not room:
        vacancy += 1
print("Vacancies in 2 - 14:", vacancy)
