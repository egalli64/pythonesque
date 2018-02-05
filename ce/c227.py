"""
Real fake
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-real-fake.html
      https://www.codeeval.com/open_challenges/227/
"""

import sys


def solution(line):
    numbers = [int(c) for c in line if c.isdigit()]
    result = 0
    for i in range(len(numbers)):
        result += numbers[i] if i%2 else numbers[i] * 2
    return 'Fake' if result % 10 else 'Real'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')