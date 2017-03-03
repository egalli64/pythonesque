"""
CodeEval Multiples of a Number
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/18/
"""
import sys


def solution(line):
    target, base = map(int, line.split(','))
    result = base
    while target > result:
        result += base
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
