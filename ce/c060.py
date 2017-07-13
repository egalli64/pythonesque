"""
CodeEval Grid Walk
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/60/
"""
from collections import deque


def internal_sum(number):
    number = abs(number)
    result = 0
    while number:
        result += number % 10
        number //= 10
    return result


def is_valid(position):
    return internal_sum(position[0]) + internal_sum(position[1]) < 20


def around(pos):
    return [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]

if __name__ == '__main__':
    visited = {(0, 0)}
    checking = deque([(0, 0)])
    while checking:
        current = checking.popleft()
        for node in around(current):
            if node not in visited and is_valid(node):
                visited.add(node)
                checking.append(node)
    print(len(visited))
