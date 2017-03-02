"""
CodeEval String Permutations
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/14/
"""
import sys
from itertools import permutations


def solution(line):
    result = [''.join(x) for x in permutations(line)]
    result.sort()
    return ','.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
