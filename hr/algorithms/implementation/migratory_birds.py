"""
HackerRank Algorithms Implementation Migratory Birds

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/migratory-birds/problem

Given an array of integers in [1..5]. Return the most popular value in it.
In case of tie, return the smallest one.
"""


def solution(data):
    results = [0] * 5
    for item in data:
        results[item-1] += 1

    highest = 0
    for cur in range(1, len(results)):
        if results[cur] > results[highest]:
            highest = cur
    return highest+1

if __name__ == '__main__':
    input()  # discard header
    sights = list(map(int, input().split()))

    print(solution(sights))