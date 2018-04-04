"""
HackerRank Algorithms Implementation Sock Merchant

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/sock-merchant/problem

Given a list of integers c

Return the number of couples having the same value
"""


def solution(data):
    pending = set()
    result = 0
    for item in data:
        if item in pending:
            result += 1
            pending.remove(item)
        else:
            pending.add(item)

    return result



if __name__ == '__main__':
    input()  # discard header
    b = list(map(int, input().split()))

    print(solution(b))