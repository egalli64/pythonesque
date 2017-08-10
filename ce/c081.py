"""
CodeEval Sum To Zero
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/81/
"""
import sys
import itertools


def solution(values):
    result = 0
    for choice in itertools.combinations(values, 4):
        if sum(choice) == 0:
            result += 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(map(int, test.split(','))))
    else:
        print('Data filename expected as argument!')
