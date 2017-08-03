"""
CodeEval Sudoku
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/78/
"""
import sys
from math import sqrt


def solution(size, values):
    for i in range(size):
        expected = list(range(1, size+1))
        for j in range(size):
            cur = values[i*size+j]
            if cur not in expected:
                return False
            else:
                expected.remove(cur)

    for j in range(size):
        expected = list(range(1, size+1))
        for i in range(size):
            cur = values[i*size+j]
            if cur not in expected:
                return False
            else:
                expected.remove(cur)

    sub = int(sqrt(size))
    for si in range(sub):
        for sj in range(sub):
            expected = list(range(1, size + 1))
            for i in range(sub):
                for j in range(sub):
                    cur = values[i*size + j + sj*(size*sub) + si * sub]
                    if cur not in expected:
                        return False
                    else:
                        expected.remove(cur)

    return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.split(';')
                lhs = int(lhs)
                rhs = list(map(int, rhs.split(',')))
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
