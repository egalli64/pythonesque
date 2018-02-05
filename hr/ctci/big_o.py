"""
HackerRank Tutorials  Cracking the Coding Interview  Time Complexity: Primality
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-big-o/
"""
import math


def solution(value):
    if value == 2:
        return True
    if value < 2 or value % 2 == 0:
        return False

    limit = int(math.sqrt(value)) + 1
    for i in range(3, limit, 2):
        if value % i == 0:
            return False
    return True


if __name__ == '__main__':
    p = int(input().strip())
    for a0 in range(p):
        n = int(input().strip())
        print('Prime' if solution(n) else 'Not prime')
