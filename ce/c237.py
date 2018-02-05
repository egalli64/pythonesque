"""
Panacea - truth or lie
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-panacea-truth-or-lie.html
      https://www.codeeval.com/open_challenges/237/
"""

import sys


def solution(line):
    data = line.split(' | ')
    hexes = [int(x, 16) for x in data[0].split()]
    bins = [int(x, 2 ) for x in data[1].split()]
    return sum(hexes) <= sum(bins)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')