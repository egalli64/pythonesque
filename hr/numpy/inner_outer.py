"""
HackerRank Python Numpy Inner and Outer

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-inner-and-outer/problem

Given two arrays, compute their inner and outer product
"""
import numpy as np

left = np.array(input().split(), int)
right = np.array(input().split(), int)

print(np.inner(left, right))
print(np.outer(left, right))
