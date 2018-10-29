"""
HackerRank Algorithms Warmup Diagonal Difference
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/diagonal-difference/problem

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

input:
1 2 3
4 5 6
9 8 9
output: 2, from |15-17|
"""


def diagonalDifference(arr):
    first = 0
    second = 0
    for i in range(len(arr)):
        first += arr[i][i]
        second += arr[i][~i]

    return abs(first-second)
