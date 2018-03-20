"""
HackerRank Python Numpy Transpose and Flatten

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

given a NxM integer array matrix (N rows and M columns), print the transpose and flatten results
"""
import numpy as np

n, m = map(int, input().split())
data = np.array([input().split() for _ in range(n)], int)

print(data.transpose())
print(data.flatten())
