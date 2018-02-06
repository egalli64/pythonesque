"""
HackerRank Cracking the Coding Interview  Binary Search: Ice Cream Parlor
(using dict instead of performing a binary search)
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/hackerrank-binary-search-ice-cream.html
      https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
"""
from collections import defaultdict


def solution(money, prices):
    counter = defaultdict(list)
    for i in range(len(prices)):
        counter[prices[i]].append(i+1)

    for price, flavors in counter.items():
        target = money - price
        if target == price:
            if len(flavors) > 1:
                return '{} {}'.format(flavors[0], flavors[1])
        else:
            others = counter.get(target)
            if others:
                result = sorted([others[0], flavors[0]])
                return '{} {}'.format(*result)


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        m = int(input().strip())
        n = int(input().strip())
        a = list(map(int, input().split()))
        print(solution(m, a))
