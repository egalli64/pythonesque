"""
CodeEval Counting Primes
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/63/
"""
import sys
import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def solution(first, last):
    result = 0
    for i in range(first, last + 1):
        for j in range(10):
            limit = math.sqrt(i)
            if PRIMES[j] > limit:
                result += 1
                break
            if i % PRIMES[j] == 0:
                break

    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = map(int, test.split(','))
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
