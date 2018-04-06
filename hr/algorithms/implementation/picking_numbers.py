"""
HackerRank Algorithms Implementation Picking Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/picking-numbers/problem

Given a list sized in [2..100] of integers in [1..99]
Return the size of the biggest subset containing elements with max difference of 1
"""


def solution(items):
    counters = [0] * 100

    for item in items:
        counters[item] += 1

    result = 0
    for i in range(2, 100):
        result = max(result, counters[i-1] + counters[i])
    return result


if __name__ == '__main__':
    input()  # discard header
    data = list(map(int, input().split()))

    print(solution(data))