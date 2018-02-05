"""
One zero, two zeros...
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-one-zero-two-zeros.html
      https://www.codeeval.com/open_challenges/217/
"""

import sys

binaries = ['0', '1', '10', '11', '100', '101', '110', '111', '1000']


def solution(line):
    count, top = map(int, line.split())
    top += 1
    for i in range(len(binaries), top):
        binaries.append(format(i, 'b'))

    result = 0
    for i in range(1, top):
        if binaries[i].count('0') == count:
            result += 1
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
