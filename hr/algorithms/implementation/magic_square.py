"""
HackerRank Algorithms Implementation Forming a Magic Square

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/magic-square-forming/problem
      http://www.mathematische-basteleien.de/magsquare.htm

Given a 3x3 integer matrix

Return its minimal distance from a magic square
"""
from itertools import chain 

MAGIC_SQUARES = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6], 
    [2, 9, 4, 7, 5, 3, 6, 1, 8], 
    [6, 7, 2, 1, 5, 9, 8, 3, 4], 
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
]


def solution(square):
    flatten = list(chain(*square))

    result = float('inf')
    for magic in MAGIC_SQUARES:
        candidate = sum(abs(lhs-rhs) for lhs, rhs in zip(magic, flatten))
        result = min(result, candidate)

    return result


if __name__ == '__main__':
    s = []
    for s_i in range(3):
       s.append([int(x) for x in input().split()])
    print(s)
    print(solution(s))