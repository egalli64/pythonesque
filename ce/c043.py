"""
CodeEval Jolly Jumpers
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenge_scores/?pkbid=43
      https://www.codeeval.com/
"""
import sys


def solution(line):
    size, *data = map(int, line.split())
    if len(data) != size:
        return False

    gaps = set()
    for i in range(1, len(data)):
        gap = abs(data[i] - data[i-1])
        if gap in gaps:
            return False
        else:
            gaps.add(gap)
    for i in range(1, size):
        if i not in gaps:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print('Jolly' if solution(test.rstrip('\n')) else 'Not jolly')
        test_cases.close()
    else:
        print('Data filename expected as argument!')
