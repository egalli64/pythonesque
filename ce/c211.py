"""
Chardonnay or Cabernet
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-chardonnay-or-cabernet.html
      https://www.codeeval.com/open_challenges/211/
"""

import sys


def solution(line):
    data = line.split(' | ')
    wines = data[0].split()

    hints = {}
    for c in data[1]:
        hints[c] = hints.get(c, 0) + 1

    result = []
    for wine in wines:
        for key in hints.keys():
            if wine.count(key) < hints.get(key):
                break
        else:
            result.append(wine)

    return ' '.join(result) if result else 'False'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')