"""
CodeEval Find Min
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/85/
"""
import sys


def solution(values):
    n, k, a, b, c, r = values
    data = [a]
    for _ in range(1, k):
        data.append((b * data[-1] + c) % r)

    for i in range(k, n):
        for j in range(k):
            if j not in data[-k:]:
                break
        data.append(j)

    return data[-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution([int(x) for x in test.split(',')]))
    else:
        print('Data filename expected as argument!')
