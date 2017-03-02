"""
CodeEval Mth To Last Element
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/10/
"""
import sys


def solution(line):
    *data, pos = line.split()
    pos = int(pos)
    if pos <= len(data):
        print(data[-pos])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            solution(test.rstrip('\n'))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
