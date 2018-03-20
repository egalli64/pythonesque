"""
HackerRank Python Numpy Zeros and Ones

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

print an array of the given shape and integer type using numpy.zeros and numpy.ones
"""
import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
