"""
CodeEval Double Squares
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/33/
"""
import sys
import math


def solution(line):
    value = int(line)
    result = 0
    for i in range(int(math.sqrt(value // 2)) + 1):
        j = math.sqrt(value - i ** 2)
        if j.is_integer():
            result += 1

    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        test_cases.readline()
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
