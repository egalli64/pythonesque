"""
CodeEval Capitalize Words
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/93/
"""
import sys


def solution(words):
    return ' '.join([x[0].capitalize() + x[1:] for x in words])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.split()))
    else:
        print('Data filename expected as argument!')
