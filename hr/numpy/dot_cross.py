"""
HackerRank Python Numpy Dot and Cross

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-dot-and-cross/problem

Given two NxN arrays, compute their matrix product
"""
import numpy as np

n = int(input())
left = np.array([input().split() for _ in range(n)], int)
right = np.array([input().split() for _ in range(n)], int)

print(np.dot(left, right))
