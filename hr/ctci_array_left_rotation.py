"""
HackerRank Tutorials  Cracking the Coding Interview  Arrays: Left Rotation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-arrays-left-rotation.html
      https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""


def solution(values, size, shift):
    return values[shift:] + values[:shift]

if __name__ == '__main__':
    n, d = map(int, (input().split()))
    data = [int(x) for x in input().split()]

    print(solution(data, n, d))