"""
CodeEval First Non-Repeated Character
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/12/
"""
import sys
from collections import Counter


def solution(line):
    count = Counter(line)
    for c in line:
        if count[c] == 1:
            return c

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
