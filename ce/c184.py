"""
Burrows-Wheeler transform
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenges/184/
      http://thisthread.blogspot.com/2017/02/codeeval-burrows-wheeler-transform.html
"""

import sys

EOL = '$'


def solution(line):
    rots = [[] for _ in line]
    for _ in line:
        for ch, rot in zip(line, rots):
            rot.insert(0, ch)
        rots.sort()

    for candidate in rots:
        if candidate[-1] == EOL:
            return ''.join(candidate)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('|\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')