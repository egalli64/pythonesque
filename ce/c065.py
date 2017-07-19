"""
CodeEval Word Search
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/65/

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where adjacent cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

"""
import sys
from collections import deque

# MATRIX = [
#     ['ABCE'],
#     ['SFCS'],
#     ['ADEE']
# ]

WHERE = {'A': {(0, 0), (2, 0)},
         'B': {(0, 1)},
         'C': {(0, 2), (1, 2)},
         'D': {(2, 1)},
         'E': {(0, 3), (2, 2), (2, 3)},
         'F': {(1, 1)},
         'S': {(1, 0), (1, 3)}}

NEIGHBORS = {
    (0, 0): {(0, 1), (1, 0)},
    (0, 1): {(0, 0), (1, 1), (0, 2)},
    (0, 2): {(0, 1), (1, 2), (0, 3)},
    (0, 3): {(0, 2), (1, 3)},

    (1, 0): {(0, 0), (1, 1), (2, 0)},
    (1, 1): {(1, 0), (0, 1), (2, 1), (1, 2)},
    (1, 2): {(1, 1), (1, 3), (0, 2), (2, 2)},
    (1, 3): {(1, 2), (0, 3), (2, 3)},

    (2, 0): {(1, 0), (2, 1)},
    (2, 1): {(2, 0), (2, 2), (1, 1)},
    (2, 2): {(2, 1), (1, 2), (2, 3)},
    (2, 3): {(2, 2), (1, 3)}
}


def find(node, visited, letters):
    if not letters:
        return True

    letter = letters.popleft()
    nodes = WHERE[letter] & NEIGHBORS[node]
    for node in nodes:
        if node not in visited:
            visited.add(node)
            if find(node, visited, letters):
                return True
            visited.remove(node)
    letters.appendleft(letter)
    return False


def solution(line):
    letters = deque(line)
    letter = letters.popleft()
    nodes = WHERE[letter]
    visited = set()
    for node in nodes:
        visited.add(node)
        if find(node, visited, letters):
            return True
        visited.remove(node)

    return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
