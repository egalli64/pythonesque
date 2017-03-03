"""
CodeEval Fibonacci Series
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/22/
"""
import sys

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]


def solution(line):
    n = int(line)
    if n < len(fibonacci):
        return fibonacci[n]
    while n >= len(fibonacci):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
