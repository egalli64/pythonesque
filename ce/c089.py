"""
CodeEval Pass Triangle
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/09/codeeval-pass-triangle.html
      https://www.codeeval.com/open_challenges/89/
"""
import sys


def solution(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(len(data[i])-1):
            data[i-1][j] += max(data[i][j], data[i][j+1])
    return data[0][0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            values = []
            for test in file:
                values.append([int(x) for x in test.split()])
            print(solution(values))
    else:
        print('Data filename expected as argument!')
