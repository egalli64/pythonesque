"""
CodeEval Point In Circle
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/98/

"""
import sys
import math
import ast


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def coordinates(chunk):
    beg = chunk.find('(')
    end = chunk.find(')')
    return ast.literal_eval(chunk[beg+1:end])


def length(chunk):
    return float(chunk.split()[1])


def solution(center, radius, point):
    return 'false' if distance(center, point) > radius else 'true'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                first, second, third = test.split(';')
                print(solution(coordinates(first), length(second), coordinates(third)))
    else:
        print('Data filename expected as argument!')
