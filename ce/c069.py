"""
CodeEval Distinct Subsequences
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/69/
"""
import sys


def count(seq, pos_s, pattern, pos_p):
    if pos_s >= len(seq) or pos_p >= len(pattern):
        return 0
    if seq[pos_s] != pattern[pos_p]:
        return count(seq, pos_s + 1, pattern, pos_p)

    result = 0
    if pos_p + 1 == len(pattern):
        result += 1
    result += count(seq, pos_s + 1, pattern, pos_p + 1)
    result += count(seq, pos_s + 1, pattern, pos_p)
    return result


def solution(seq, pattern):
    return count(seq, 0, pattern, 0)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.rstrip('\n').split(',')
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
