"""
CodeEval String List
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-string-list.html
      https://www.codeeval.com/open_challenges/38/
"""
import sys
from itertools import product


def solution(line):
    n, data = line.split(',')
    letters = sorted(list(set(data)))
    result = letters
    for i in range(int(n)-1):
        result = ['{}{}'.format(x[0], x[1]) for x in product(result, letters)]
    return ','.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
