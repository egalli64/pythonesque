"""
CodeEval Longest Common Subsequence
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-longest-common-subsequence.html
      https://www.codeeval.com/open_challenges/6/
"""
import sys


def solution(line):
    ver, hor = line.split(';')
    t = [[0 for j in range(len(hor)+1)] for i in range(len(ver)+1)]
    for i in range(len(ver)):
        for j in range(len(hor)):
            t[i + 1][j + 1] = t[i][j] + 1 if ver[i] == hor[j] else max(t[i+1][j], t[i][j+1])

    i, j = len(ver), len(hor)
    result = [None] * t[i][j]
    cur = -1

    while i > 0 and j > 0:
        if t[i][j] == t[i-1][j]:
            i -= 1
        elif t[i][j] == t[i][j-1]:
            j -= 1
        else:
            result[cur] = ver[i-1]
            cur -= 1
            i -= 1
            j -= 1

    return ''.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
