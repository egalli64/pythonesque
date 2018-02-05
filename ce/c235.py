"""
Simple or trump
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-simple-or-trump.html
      https://www.codeeval.com/open_challenges/235/
"""

import sys


def values(cards, trump):
    result = [0, 0]
    for i in [0, 1]:
        suit = cards[i][-1]
        value = cards[i][:-1]
        if value == 'J':
            result[i] = 11
        elif value == 'Q':
            result[i] = 12
        elif value == 'K':
            result[i] = 13
        elif value == 'A':
            result[i] = 14
        else:
            result[i] = int(value)

        if suit == trump:
            result[i] *= 10
    return result


def solution(line):
    data = line.split(' | ')
    faces = data[0].split()
    cards = values(faces, data[1])
    if cards[0] > cards[1]:
        return faces[0]
    if cards[1] > cards[0]:
        return faces[1]
    return data[0]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')