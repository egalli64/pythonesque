"""
HackerRank Python Numpy Eye and Identity

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-eye-and-identity/problem

print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else
"""
import numpy as np

n, m = map(int, input().split())

if n == m:
    # just to use identity too
    print(np.identity(n))
else:
    print(np.eye(n, m))
