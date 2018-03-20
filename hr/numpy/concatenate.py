"""
HackerRank Python Numpy Concatenate

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-concatenate/problem

given two integer arrays of size NxP and PxM, concatenate the arrays along axis 0.
"""
import numpy as np

n, m, _ = map(int, input().split())
left = np.array([input().split() for _ in range(n)], int)
right = np.array([input().split() for _ in range(m)], int)

print(np.concatenate((left, right)))
