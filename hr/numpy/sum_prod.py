"""
HackerRank Python Numpy Sum and Prod

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-sum-and-prod/problem

Given an NxM array, sum() it over axis 0 and then find the product of that result
"""
import numpy as np

n, _ = map(int, input().split())
values = np.array([input().split() for _ in range(n)], int)

print(np.sum(values, 0).prod())
