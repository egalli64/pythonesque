"""
CodeEval Simple Sorting
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/91/
"""
import sys


def solution(data):
    data.sort()
    return ' '.join(['{:.3f}'.format(x) for x in data])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution([float(x) for x in test.split()]))
    else:
        print('Data filename expected as argument!')
