"""
HackerRank Algorithms Warmup Mini-Max Sum
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/mini-max-sum/problem

Given five positive integers,
find the minimum and maximum values that can be calculated
 by summing exactly four of the five integers
"""


def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))
