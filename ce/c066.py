"""
CodeEval Pascals Triangle
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenges/66/
      https://www.codeeval.com/
"""
import sys


def solution(depth):
    results = []

    for i in range(depth):
        value = 1
        for k in range(i+1):
            results.append(value)
            value = value * (i - k) // (k + 1)

    return ' '.join(map(str, results))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(int(test)))
    else:
        print('Data filename expected as argument!')
