"""
CodeEval Reverse Groups
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/71/
"""
import sys


def solution(items, cycle):
    results = []
    for i in range(len(items) // cycle):
        results.extend(reversed(items[i*cycle:(i+1)*cycle]))
    results.extend(items[(i+1)*cycle:])
    return ','.join(results)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.split(';')
                lhs = lhs.split(',')
                print(solution(lhs, int(rhs)))
    else:
        print('Data filename expected as argument!')
