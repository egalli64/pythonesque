"""
CodeEval Self Describing Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-self-describing-numbers.html
      https://www.codeeval.com/open_challenges/40/
"""
import sys
from collections import Counter


def solution(line):
    counter = Counter(map(int, line))
    return int(all(counter[i] == int(line[i]) for i in range(len(line))))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
