"""
HackerRank Python Numpy Polynomials

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-polynomials/problem

given the coefficients of a polynomial, find its value at x
"""
import numpy as np

values = tuple(map(float, input().split()))
x = float(input())

print(np.polyval(values, x))
