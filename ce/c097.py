"""
CodeEval Find A Writer
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/97/
"""
import sys


def solution(encoded, indices):
    result = []
    for i in indices:
        result.append(encoded[i])
    return ''.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                first, second = test.split('|')
                print(solution(first, [int(x)-1 for x in second.split()]))
    else:
        print('Data filename expected as argument!')
