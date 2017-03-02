"""
CodeEval Lowest Common Ancestor
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/11/
"""
import sys

levels = {'30': 1, '52': 1, '8': 2, '3': 2, '10': 3, '20': 3, '29': 3}
ancestors = {1: '30', 2: '8', 3: '20'}


def solution(line):
    first, second = line.split()
    return ancestors[min(levels[first], levels[second])]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
