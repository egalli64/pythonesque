"""
HackerRank Cracking the Coding Interview Bit Manipulation: Lonely Integer
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-lonely-integer
"""


def solution(data):
    """ get the unique not-paired element in data - clean input data expected """
    results = set()
    for i in data:
        if i in results:
            results.remove(i)
        else:
            results.add(i)

    return results.pop()


if __name__ == '__main__':
    input()  # skip header
    values = [int(x) for x in input().split()]

    print(solution(values))
