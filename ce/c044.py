"""
CodeEval Following Integer
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-following-integer.html
      https://www.codeeval.com/open_challenges/44/
"""
import sys
from itertools import permutations
from bisect import insort


def solution(line):
    digits = []
    for c in line:
        if c != '0':
            insort(digits, c)
    while len(digits) <= len(line):
        digits.insert(1, '0')
    result = int(''.join(digits))

    current = int(line)
    for item in permutations(line):
        candidate = int(''.join(item))
        if result > candidate > current:
            result = candidate

    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
