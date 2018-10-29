"""
HackerRank Algorithms Warmup Compare the Triplets
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""


def compareTriplets(a, b):
    left = 0
    right = 0

    for lhs, rhs in zip(a, b):
        if lhs > rhs:
            left += 1
        elif rhs > lhs:
            right += 1
    
    return (left, right)
