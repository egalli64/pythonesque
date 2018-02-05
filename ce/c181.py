"""
Gronsfeld cipher
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-gronsfeld-cipher.html
      https://www.codeeval.com/open_challenges/181/
"""

import sys

ALPHA = ' !"#$%&\'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def solution(line):
    data = line.split(';')
    data[0] = [int(x) for x in data[0]]

    result = []
    for i in range(len(data[1])):
        result.append(ALPHA[ALPHA.index(data[1][i]) - data[0][i % len(data[0])]])
    return ''.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')