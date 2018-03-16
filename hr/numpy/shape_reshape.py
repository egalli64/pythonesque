"""
HackerRank Python Numpy Shape and Reshape

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-shape-reshape/problem

given a space separated list of nine integers, convert it to a 3x3 NumPy array
"""
import numpy as np


def solution(data):
    return np.array(data).reshape(3, 3)


if __name__ == '__main__':
    print(solution([int(x) for x in input().split()]))
