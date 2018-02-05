"""
Filename Pattern
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-filename-pattern.html
      https://www.codeeval.com/open_challenges/169/
"""

import sys
import re


def adjust(pattern):
    return re.sub('\*', '.*', re.sub('\?', '.', re.sub('\.', '\.', pattern))) + '$'


def solution(line):
    data = line.split()
    pattern = adjust(data.pop(0))
    result = [name for name in data if re.match(pattern, name)]
    return ' '.join(result) if result else '-'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')