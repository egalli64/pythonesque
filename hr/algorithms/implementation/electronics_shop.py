"""
HackerRank Algorithms Implementation Electronics Shop

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/electronics-shop/problem

Given, as integers:
- s: total available amount
- ks: list of prices for available keyboards
- ds: list of prices for available drives

Return the more expensive choice of a single "k" and a single "d", or -1
"""
from itertools import product

def solution2(keyboards, drives, amount):
    return max((k+d if k+d <= amount else -1 for k, d in product(keyboards, drives)))


def solution(keyboards, drives, amount):
    result = -1
    
    for k in keyboards:
        for d in drives:
            candidate = k + d
            if candidate <= amount and candidate > result:
                result = candidate

    return result


if __name__ == '__main__':
    s, _, _ = map(int, input().split())
    ks = list(map(int, input().split()))
    ds = list(map(int, input().split()))

    print(solution(ks, ds, s))