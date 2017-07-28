"""
CodeEval Minimum Path Sum
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/72/
"""
import sys
import math


def solution(data):
    dp = [[float(math.inf)] * (len(data) + 1)]
    for i in range(len(data)):
        dp.append([math.inf])
        dp[i+1].extend(data[i])

    end = len(dp)
    for i in range(1, end):
        for j in range(1, end):
            if i == 1 and j == 1:
                continue
            dp[i][j] += min(dp[i-1][j], dp[i][j-1])
    return dp[i][j]


def solution_2(data):
    last = len(data) - 1
    for i in range(last, -1, -1):
        for j in range(last, -1, -1):
            if i == last and j == last:
                continue
            if i == last:
                data[i][j] += data[i][j+1]
            elif j == last:
                data[i][j] += data[i+1][j]
            else:
                data[i][j] += min(data[i + 1][j], data[i][j+1])
    return data[0][0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            while True:
                matrix = []
                size = file.readline()
                if not size:
                    break
                for _ in range(int(size)):
                    line = [int(x) for x in file.readline().split(',')]
                    matrix.append(line)

                print(solution_2(matrix))
    else:
        print('Data filename expected as argument!')
