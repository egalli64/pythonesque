"""
Mersenne prime
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-mersenne-prime.html
      https://www.codeeval.com/open_challenges/240/
"""

import sys
from math import sqrt

marsennes = [(2, 3)]


def is_prime(number):
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def trim(value):
    i = 0
    while marsennes[i][1] < value:
        i += 1
    return marsennes[:i]


def get_marsennes(value):
    if value <= marsennes[-1][1]:
        return trim(value)

    index = marsennes[-1][0]
    while True:
        index += 1
        if not is_prime(index):
            continue

        marsenne = 2**index - 1
        marsennes.append((index, marsenne))

        if marsenne < value:
            continue
        return marsennes if marsenne == value else marsennes[:-1]


def solution(line):
    value = int(line)
    result = get_marsennes(value)
    return ', '.join(map(str, [r[1] for r in result]))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')