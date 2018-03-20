"""
HackerRank Python Numpy Floor, Ceil and Rint

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

print floor, ceil and rint for the values in an array
"""
import numpy as np

values = np.array(input().split(), float)

print(np.floor(values))
print(np.ceil(values))
print(np.rint(values))
