"""
HackerRank Algorithms Implementation Breaking the Records

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

Given a list of scores, print the number of breaks the records up and down
"""


def solution(scores):
    increases = 0
    decreases = 0

    higher = lower = scores[0]
    for score in scores[1:]:
        if score > higher:
            higher = score
            increases += 1
        elif score < lower:
            lower = score
            decreases += 1

    return increases, decreases


if __name__ == '__main__':
    input()  # discard header
    items = list(map(int, input().split()))

    print(*solution(items))