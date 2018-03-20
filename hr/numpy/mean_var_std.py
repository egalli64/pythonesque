"""
HackerRank Python Numpy Mean, Var, and Std

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

Given an NxM array, print:
The mean along axis 1
The var along axis 0
The full std
"""
import numpy as np

n, _ = map(int, input().split())
values = np.array([input().split() for _ in range(n)], int)

print(np.mean(values, 1))
print(np.var(values, 0))
print(np.std(values))
