"""
CodeEval Bit Positions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/19/
"""
import sys


def solution(line):
    n, *bits = map(int, line.split(','))
    b1 = bool(n & 2 ** (bits[0]-1))
    b2 = bool(n & 2 ** (bits[1]-1))
    return str(not(b1 ^ b2)).lower()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
