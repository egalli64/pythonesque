"""
HackerRank Cracking the Coding Interview  Binary Search: Ice Cream Parlor
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/hackerrank-binary-search-ice-cream.html
      https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
"""


def find_other(counter, pos, price):
    left = pos+1
    right = len(counter)-1
    while left <= right:
        mid = (left + right) // 2
        if counter[mid][0] == price:
            return counter[mid][1]

        if counter[mid][0] > price:
            right = mid-1
        else:
            left = mid+1
    return None


def solution(money, prices):
    counter = sorted([(price, flavor+1) for flavor, price in enumerate(prices)])
    for i in range(len(counter)):
        other = find_other(counter, i, money - counter[i][0])
        if other:
            result = sorted([counter[i][1], other])
            return '{} {}'.format(*result)


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        m = int(input().strip())
        n = int(input().strip())
        a = list(map(int, input().split()))
        print(solution(m, a))
