"""
CodeEval Detecting Cycles
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-detecting-cycles.html
      https://www.codeeval.com/open_challenges/5/
"""
import sys


def solution(line):
    data = line.split()
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] != data[j]:
                continue

            size = min(j - i, len(data) - j)
            for k in range(1, size):
                if data[i+k] != data[j+k]:
                    size = k
                    break
            return ' '.join(data[i:i+size])
    return ''

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
