"""
CodeEval Happy Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-happy-numbers.html
      https://www.codeeval.com/open_challenges/39/
"""
import sys


def squared_ciphers(number):
    while number:
        number, cipher = divmod(number, 10)
        yield cipher ** 2


def solution(line):
    candidate = int(line)
    explored = set()
    while candidate != 1:
        if candidate in explored:
            return 0
        explored.add(candidate)
        candidate = sum(squared_ciphers(candidate))
    return 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
