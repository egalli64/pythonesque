"""
Clean up the words
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-clean-up-words.html
      https://www.codeeval.com/open_challenges/205/
"""

import sys
import re


def solution_almost_c(line):
    result = []
    alpha = False

    for c in line:
        if c.isalpha():
            alpha = True
            result.append(c.lower())
        elif alpha:
            result.append(' ')
            alpha = False

    if result:
        result.pop()

    return ''.join(result)


def solution(line):
    return re.sub('[^a-zA-Z]+', ' ', line).lower().strip()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')