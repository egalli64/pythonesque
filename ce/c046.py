"""
CodeEval Prime Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/46/
"""
import sys

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_prime(number):
    for prime in primes:
        if prime ** 2 > number:
            return True
        if number % prime == 0:
            return False


def solution(line):
    ceil = int(line)
    if ceil < 3:
        print()
        return
    print(2, sep='', end='')

    for prime in primes:
        if prime >= ceil:
            print()
            return
        print(',', prime, sep='', end='')

    for i in range(primes[-1] + 2, ceil, 2):
        if is_prime(i):
            primes.append(i)
            print(',', i, sep='', end='')
    print()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                solution(test.rstrip('\n'))
    else:
        print('Data filename expected as argument!')
