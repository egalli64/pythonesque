"""
CodeEval Pangrams
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/37/
"""
import sys
from string import ascii_lowercase


def solution(line):
    target = set(line.lower())
    result = []
    for c in ascii_lowercase:
        if c not in target:
            result.append(c)
    return ''.join(result) if result else 'NULL'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
