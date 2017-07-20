"""
CodeEval Valid Parentheses
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/68/
"""
import sys
from collections import deque

MATCHES = {')': '(', ']': '[', '}': '{'}


def solution(line):
    buffer = deque()

    for c in line:
        if c in MATCHES.values():
            buffer.append(c)
        elif len(buffer) and c in MATCHES.keys() and buffer[-1] == MATCHES[c]:
            buffer.pop()
        else:
            return False

    return len(buffer) == 0

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
