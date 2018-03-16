"""
HackerRank Python Numpy Arrays

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-arrays/problem

given a space separated list of numbers, print a reversed NumPy array with the element type float
"""
import numpy as np


def solution(arr):
    return np.array(arr[::-1], float)


if __name__ == '__main__':
    print(solution(input().split()))
