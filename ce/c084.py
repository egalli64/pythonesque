"""
CodeEval Balanced Smileys
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/08/codeeval-balanced-smileys.html
      https://www.codeeval.com/open_challenges/84/
"""
import sys


def solution(msg):
    min_open = 0
    max_open = 0
    for i in range(len(msg)):
        if msg[i] == '(':
            max_open += 1
            if i == 0 or msg[i-1] != ':':
                min_open += 1
        elif msg[i] == ')':
            if i == 0:
                return False
            min_open = min_open - 1 if min_open else 0
            if msg[i-1] != ':':
                if max_open == 0:
                    return False
                max_open -= 1
    return True if min_open == 0 else False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print('YES' if solution(test.rstrip('\n')) else 'NO')
    else:
        print('Data filename expected as argument!')
