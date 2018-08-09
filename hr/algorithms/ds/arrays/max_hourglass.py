"""
HackerRank Algorithms Data Structures Arrays 2D Array DS
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/2d-array/problem

Given a 6x6 matrix of numbers in [-9, 9] return the max value hourglass in it
"""


def solution(data):
    assert len(data) == 6 and len(data[0]) == 6

    result = -9 * 7
    for i in range(4):
        for j in range(4):
            candidate = (data[i][j] + data[i][j+1] + data[i][j+2] + data[i+1][j+1] 
                + data[i+2][j] + data[i+2][j+1] + data[i+2][j+2])
            result = max(result, candidate)
    return result


if __name__ == '__main__':
    data = [list(map(int, input().split())) for _ in range(6)]
    print(solution(data))