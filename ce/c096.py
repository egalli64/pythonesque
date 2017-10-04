"""
CodeEval Swap Case
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/96/
"""
import sys


def solution(line):
    result = []
    for c in line:
        if c.islower():
            result.append(c.upper())
        else:
            result.append(c.lower())
    return ''.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
