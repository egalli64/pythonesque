"""
Testing
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-testing.html
      https://www.codeeval.com/open_challenges/225/
"""

import sys


def solution(line):
    data = line.split(' | ')

    bugs = 0
    for i in range(len(data[0])):
        if data[0][i] != data[1][i]:
            bugs += 1

    if bugs == 0:
        return 'Done'
    elif bugs < 3:
        return 'Low'
    elif bugs < 5:
        return 'Medium'
    elif bugs < 7:
        return 'High'
    else:
        return 'Critical'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')