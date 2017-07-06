"""
CodeEval Robot Movements
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/56/
"""
board = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

beg = (0, 0)
end = (3, 3)


def solution(pos):
    if board[pos[0]][pos[1]]:
        return 0
    if pos == end:
        return 1

    board[pos[0]][pos[1]] = True
    result = 0
    if pos[0] > 0:
        result += solution((pos[0] - 1, pos[1]))
    if pos[0] < end[0]:
        result += solution((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        result += solution((pos[0], pos[1] - 1))
    if pos[1] < end[1]:
        result += solution((pos[0], pos[1] + 1))

    board[pos[0]][pos[1]] = False
    return result


if __name__ == '__main__':
    print(solution(beg))
