"""
HackerRank Python Numpy Array Mathematics

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-array-mathematics/problem

Given two arrays of dimensions NxM, print the results of
add(), subtract(), multiply(), divide(), mod(), power()
"""
import numpy as np

n, _ = map(int, input().split())

left = np.array([input().split() for _ in range(n)], int)
right = np.array([input().split() for _ in range(n)], int)

print(left + right)
print(left - right)
print(left * right)
print(left // right)
print(left % right)
print(left ** right)
