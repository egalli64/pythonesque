# Strings and arrows
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/codeeval-strings-and-arrows.html
#       https://www.codeeval.com/open_challenges/203/


import sys

ARROWS = ['>>-->', '<--<<']
ARROW_SIZE = 5


def solution(line):
    result = 0
    for i in range(len(line)):
        candidate = line[i:i + ARROW_SIZE]
        if candidate in ARROWS:
            result += 1
    return result


def solution_skip(line):
    result = 0
    i = 0
    while i < len(line):
        candidate = line[i:i + ARROW_SIZE]
        if candidate in ARROWS:
            result += 1
            i += ARROW_SIZE - 1
        else:
            i += 1
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')