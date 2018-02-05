"""
Template for Python 3 problems by CodeEval
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-time-to-eat.html
      https://www.codeeval.com/open_challenges/214/
"""

import sys


def solution(line):
    return ' '.join(sorted(line.split(), reverse=True))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')