"""
Black card
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-black-card.html
      https://www.codeeval.com/open_challenges/222/
"""

import sys


def solution(line):
    data = line.split(' | ')
    players = data[0].split()
    black = int(data[1]) - 1

    while len(players) > 1:
        del players[black if black < len(players) else black % len(players)]
    return players[0]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')