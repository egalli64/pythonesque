"""
CodeEval Calculate Distance
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/99/

"""
import sys
import math
import ast


def distance(a, b):
    return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))


def make_tuple(chunk):
    return ast.literal_eval(chunk)


def solution(line):
    pos = line.find(') (') + 1
    return distance(make_tuple(line[:pos]), make_tuple(line[pos+1:]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test))
    else:
        print('Data filename expected as argument!')
