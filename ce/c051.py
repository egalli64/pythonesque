"""
CodeEval Closest Pair
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/51/
Brute force solution is good enough.
"""
import sys
from math import sqrt

MAX = 10000 ** 2


def solution(pts):
    squared_result = MAX
    for i in range(len(pts) - 1):
        for j in range(i+1, len(pts)):
            tentative = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
            if tentative < squared_result:
                squared_result = tentative
    return 'INFINITY' if squared_result == MAX else '{:.4f}'.format(sqrt(squared_result))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            while True:
                size = int(file.readline())
                if size == 0:
                    break

                points = []
                for i in range(size):
                    points.append(tuple(map(int, file.readline().split())))
                print(solution(points))
    else:
        print('Data filename expected as argument!')
