"""
CodeEval Number of Ones
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/16/
"""
import sys


def solution(value):
    result = 0
    while value:
        if value & 1:
            result += 1
        value >>= 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(int(test.rstrip('\n'))))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
