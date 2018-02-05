"""
Number Operations
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-number-operations.html
      https://www.codeeval.com/open_challenges/190/
"""
import sys
from itertools import permutations, product


def solution(line):
    data = [int(x) for x in line.split()]
    for numbers in permutations(data):
        for operations in product('*+-', repeat=4):
            result, *values = numbers
            for value, op in zip(values, operations):
                if op == '+':
                    result += value
                elif op == '-':
                    result -= value
                else:
                    result *= value
            if result == 42:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')