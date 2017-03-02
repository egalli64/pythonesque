"""
CodeEval Sum of integers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-sum-of-integers.html
      https://www.codeeval.com/open_challenges/17/
"""
import sys


def solution(line):
    head, *values = [int(x) for x in line.split(',')]

    result = head
    maybe = head
    for value in values:
        maybe = value if maybe < 0 else maybe + value
        if maybe > result:
            result = maybe
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
