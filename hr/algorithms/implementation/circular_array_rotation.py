"""
HackerRank Algorithms Implementation Circular Array Rotation

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/circular-array-rotation/problem

Given a list of integers a number of rotations k and an index m
Return the list element at position m after k rotations
"""


def solution(data, rotations, index):
    pos = (index - rotations) % len(data)
    return data[pos]


if __name__ == '__main__':
    _, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        print(solution(a, k, int(input())))
