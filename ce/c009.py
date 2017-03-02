"""
CodeEval Stack Implementation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/9/
"""
import sys


def solution(line):
    data = line.split()
    result = []
    for i in range(-1, -(len(data)+1), -2):
        result.append(data[i])
    return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
