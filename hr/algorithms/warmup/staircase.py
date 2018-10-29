"""
HackerRank Algorithms Warmup Staircase
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/staircase/problem

Write a program that prints a staircase of size n
"""


def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '#' * i)
