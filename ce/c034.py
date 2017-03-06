"""
CodeEval Number Pairs
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/34/
"""
import sys
from _bisect import bisect_left


def solution(line):
    data, total = line.split(';')
    data = [int(x) for x in data.split(',')]
    total = int(total)
    result = []
    for i in range(len(data)):
        if data[i] * 2 >= total:
            break
        target = total - data[i]
        j = bisect_left(data, target, i+1)
        if j != len(data) and data[j] == target:
            result.append((data[i], data[j]))
    if not result:
        return 'NULL'
    return ';'.join('{},{}'.format(x[0], x[1]) for x in result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
