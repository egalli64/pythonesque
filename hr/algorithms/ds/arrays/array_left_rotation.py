"""
HackerRank  Data Structures  Arrays  Left Rotation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/array-left-rotation/problem

perform a n-left rotations on the passed array
"""


def solution(data, rot):
    return data[rot:] + data[:rot]


if __name__ == '__main__':
    _, n = map(int, input().split())
    data = input().split()
    print(' '.join(solution(data, n)))