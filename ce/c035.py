"""
CodeEval Email Validation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/35/
"""
import sys
import re


def solution(line):
    pattern = '(^"[@\._a-zA-Z1-9]+"|[\+\._a-zA-Z1-9])+@[\._a-zA-Z1-9]+.[a-z]+$'
    return 'true' if re.match(pattern, line) else 'false'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
