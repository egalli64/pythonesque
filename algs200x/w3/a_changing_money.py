"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 3 - greedy algorithms: Changing Money
Find the minimum number of coins needed to change the input value into coins with denominations 1, 5, and 10
"""
DENOMINATIONS = [10, 5, 1]


def solution(total):
    leftover = total
    result = 0

    for coin in DENOMINATIONS:
        counter = leftover // coin
        if counter > 0:
            result += counter
            leftover %= coin

        if leftover == 0:
            break

    return result
