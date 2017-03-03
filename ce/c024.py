"""
CodeEval Sum of Integers from File
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/24/
"""
import sys


def solution(line):
    pass

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    result = 0
    for test in test_cases:
        result += int(test.rstrip('\n'))
    print(result)
    test_cases.close()
