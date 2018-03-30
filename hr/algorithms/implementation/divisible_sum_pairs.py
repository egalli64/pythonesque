"""
HackerRank Algorithms Implementation Divisible Sum Pairs

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/03/hackerrank-divisible-sum-pairs.html
      https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

Given an integer k and a list of integers
Returns the number of couples having sum divisible by k
"""


def solution_naive(k, values):
    result = 0
    for i in range(len(values) - 1):
        for j in range(i+1, len(values)):
            if (values[i] + values[j]) % k == 0:
                result += 1
    return result


def solution(k, values):
    remainders = [0] * k
    for i in range(len(values)):
        remainders[values[i] % k] += 1

    result = remainders[0] * (remainders[0] - 1) // 2

    pivot = k // 2
    if k%2:
        pivot += 1
    else:
        result += remainders[k//2] * (remainders[k//2] - 1) // 2

    for i in range(1, pivot):
        result += remainders[i] * remainders[k-i]

    return result


if __name__ == '__main__':
    _, k = map(int, input().split())
    items = list(map(int, input().split()))

    print(solution(k, items))
