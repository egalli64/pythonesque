"""
Not So Clever
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-not-so-clever.html
      https://www.codeeval.com/open_challenges/232/
"""

import sys


def split(line):
    data, steps = line.split(' | ')
    return [int(i) for i in data.split()], int(steps)


def solution(line):
    data, steps = split(line)
    for i in range(steps):
        for j in range(1, len(data)):
            if data[j] < data[j-1]:
                data[j-1], data[j] = data[j], data[j-1]
                break
    return ' '.join(str(c) for c in data)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')