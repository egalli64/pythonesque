"""
CodeEval Simple Calculator
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenges/94/
      https://www.codeeval.com/

Filthy cheating: use of eval was forbidden!
"""
import sys


def solution(line):
    result = eval(line.replace('^', '**'))
    return int(result) if type(result) is int or result.is_integer() else "{:.5f}".format(result).rstrip('0')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
