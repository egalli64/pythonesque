"""
HackerRank Algorithms Implementation Angry Professor

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/angry-professor/problem

Given k in [1 .. 1000] and a list of integers in [-100 .. 100]
Return YES if at least k elements are non positive, NO otherwise
"""


def solution(k, items):
    ok = 0
    for item in items:
        if item <= 0:
            ok += 1
    return 'YES' if k > ok else 'NO'


if __name__ == '__main__':
    for _ in range(int(input())):
        _, k = map(int, input().split())
        data = list(map(int, input().split()))
        print(solution(k, data))