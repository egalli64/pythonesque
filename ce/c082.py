"""
CodeEval Armstrong Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/82/
"""
import sys


def solution(value, exp):
    cubes = 0
    cache = value
    while value:
        cur = value % 10
        value //= 10
        cubes += cur ** exp
    return cache == cubes

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(int(test), len(test) - 1))
    else:
        print('Data filename expected as argument!')
