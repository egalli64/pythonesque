"""
HackerRank Python Numpy Min and Max

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-min-and-max/problem

Given an NxM array, min() it over axis 1 and then find the max of that
"""
import numpy as np

n, _ = map(int, input().split())
values = np.array([input().split() for _ in range(n)], int)

print(np.min(values, 1).max())
