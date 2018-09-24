"""
HackerRank  Data Structures  Arrays  Array Manipulation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/09/hackerrank-array-manipulation.html
      https://www.hackerrank.com/challenges/crush/problem

Create a list of zeroes sized n and apply m transformations on it
Each trasformation is a plain addition in the inclusive (one-based) range [a, b] by k
Return the highest value in the list
"""
import itertools


class NaiveManipulator:
    def __init__(self, sz):
        self.data = [0] * sz
    
    def set(self, first, last, value):
        for i in range(first-1, last):
            self.data[i] += value

    def solution(self):
        return max(self.data)


class ArrayManipulator:
    def __init__(self, sz):
        self.data = [0] * (sz + 2)
    
    def set(self, first, last, value):
        self.data[first] += value
        self.data[last+1] -= value

    def solution(self):
        return max(itertools.accumulate(self.data))


def set_delta(data, first, last, value):
    data[first] += value
    data[last+1] -= value


def solution(data):
    return max(itertools.accumulate(data))


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [0] * (n + 2)

    for _ in range(m):
        a, b, k = map(int, input().split())
        set_delta(data, a, b, k)

    print(solution(data))
