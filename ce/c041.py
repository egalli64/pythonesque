"""
CodeEval Array Absurdity
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/41/
"""
import sys


def solution(line):
    data = [int(x) for x in line.split(';')[1].split(',')]
    values = set()
    for value in data:
        if value in values:
            return value
        else:
            values.add(value)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
