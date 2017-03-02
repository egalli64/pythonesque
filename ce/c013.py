"""
CodeEval Remove Characters
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/13/
"""
import sys


def solution(line):
    *words, extra = line.split(', ')
    result = []
    for word in words:
        combed = [c for c in word if c not in extra]
        result.append(''.join(combed))
    return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
