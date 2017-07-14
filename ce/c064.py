"""
CodeEval Climbing Stairs
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/64/
"""
import sys


def solution(steps):
    a, b = 0, 1
    for i in range(steps + 1):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(int(test)))
    else:
        print('Data filename expected as argument!')
