"""
HackerRank Cracking the Coding Interview DP: Coin Change
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/03/hackerrank-dp-coin-change.html
      https://www.hackerrank.com/challenges/ctci-coin-change/problem

Get the number of different ways you can make change for dollars if each coin is available in an infinite quantity
"""


def solution_full(denominations, total):
    table = [[0] * (total + 1) for _ in range(len(denominations) + 1)]
    table[0][0] = 1

    for i in range(1, len(denominations) + 1):
        for j in range(total+1):
            table[i][j] += table[i - 1][j]
            cur = denominations[i-1]
            if cur <= j:
                table[i][j] += table[i][j-cur]

    return table[-1][-1]


def solution(denominations, total):
    cache = [0] * (total + 1)
    cache[0] = 1

    for denomination in denominations:
        for j in range(denomination, total+1):
            cache[j] += cache[j-denomination]
    return cache[-1]


if __name__ == '__main__':
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
    print(solution(coins, n))
