"""
CodeEval Unique Elements
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/29/
"""
import sys


def solution(line):
    first, *data = line.split(',')
    result = [first]
    for item in data:
        if item != result[-1]:
            result.append(item)
    return ','.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
