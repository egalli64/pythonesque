"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Final Project - Tic-Tac-Toe

    the computer is 'X'
    the user is 'O'
    the first move belongs to the computer it always puts its first 'X' in the middle of the board
    squares are numbered row by row starting with 1
    the user input is done by entering the number of the square they choose - the number must be valid
    check if the game is over, possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
    the computer responds with its move and the check is repeated;
    a random field choice made by the computer is good enough for the game.
"""
from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    while True:
        move = int(input("Enter your move: "))
        if 1 <= move <= 9:
            move -= 1
            i = move // 3
            j = move % 3
            if board[i][j] not in ['O', 'X']:
                board[i][j] = 'O'
                return

        print("Try again!")


def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['O', 'X']:
                free.append((i, j))
    return free


def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        return None

    cross1 = cross2 = True
    for k in range(3):
        if board[k][0] == sgn and board[k][1] == sgn and board[k][2] == sgn:
            return who
        if board[0][k] == sgn and board[1][k] == sgn and board[2][k] == sgn:
            return who
        if board[k][k] != sgn:
            cross1 = False
        if board[2 - k][2 - k] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        chosen = randrange(cnt)
        i, j = free[chosen]
        board[i][j] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")
