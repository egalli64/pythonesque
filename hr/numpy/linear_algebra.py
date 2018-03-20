"""
HackerRank Python Numpy Linear Algebra

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-linear-algebra/problem

You are given a square matrix with dimensions N, print its determinant.
"""
import numpy as np

n = int(input())
values = np.array([input().split() for _ in range(n)], float)

print(np.linalg.det(values))
