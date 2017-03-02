"""
CodeEval Prefix Expressions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-prefix-expressions.html
      https://www.codeeval.com/open_challenges/7/
"""
import sys

mapping = {'+': lambda r, v: r + v, '*': lambda r, v: r * v, '/': lambda r, v: r / v}


def solution(line):
    data = line.split()
    i = len(data) // 2
    result = float(data[i])
    for op, value in zip(reversed(data[0:i]), data[i + 1:]):
        result = mapping[op](result, int(value))
    return int(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
