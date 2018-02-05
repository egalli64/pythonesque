"""
Consecutive Primes
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-consecutive-primes.html
      https://www.codeeval.com/open_challenges/187/
"""
import sys

PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}


def necklaces(beads, pos):
    if len(beads) == pos:
        return 1 if 1 + beads[- 1] in PRIMES else 0

    result = 0

    if beads[pos] + beads[pos-1] in PRIMES:
        result += necklaces(beads, pos + 1)

    for i in range(pos+2, len(beads), 2):
        if beads[pos-1] + beads[i] in PRIMES:
            beads[i], beads[pos] = beads[pos], beads[i]
            result += necklaces(beads, pos + 1)
            beads[i], beads[pos] = beads[pos], beads[i]

    return result


def solution(line):
    size = int(line)
    if size % 2:
        return 0
    return necklaces([x for x in range(1, size + 1)], 1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
