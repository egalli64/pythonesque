"""
CodeEval Decode Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/73/
"""
import sys


def case_2(value):
    return 1 if value < 27 else 0


def case_3(value):
    result = 0
    if value / 10 < 27:
        result += 1
    if value % 100 < 27:
        result += 1
    return result


def case_4(value):
    result = 0
    if value / 100 < 27:
        result += 1
    if value % 100 < 27:
        result += 1
    if value / 100 < 27 and value % 100 < 27:
        result += 1
    if value % 1000 / 10 < 27:
        result += 1
    return result

CASES = {1: lambda v: 0, 2: lambda v: case_2(v), 3: lambda v: case_3(v), 4: lambda v: case_4(v)}


def solution(line):
    result = 1
    value = int(line)

    try:
        result += CASES[len(line)](value)
    except KeyError:
        # unexpected!
        return 0

    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
