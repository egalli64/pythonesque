"""
CodeEval Minimum Coins
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/74/
"""
import sys


def solution(total):
    result = 0
    for coin in [5, 3, 1]:
        while coin <= total:
            result += 1
            total -= coin
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(int(test)))
    else:
        print('Data filename expected as argument!')
