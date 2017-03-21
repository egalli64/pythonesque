"""
CodeEval Repeated Substring
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/53/
"""
import sys


def solution(line):
    for size in range(len(line) // 2, 0, -1):
        for i in range(0, len(line) - 2 * size + 1):
            candidate = line[i: i + size]
            leftover = line[i + size:]
            if candidate in leftover and candidate.strip():
                return candidate
    return 'NONE'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
