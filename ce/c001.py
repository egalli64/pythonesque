# Fizz Buzz
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/fizz-buzz.html
#       https://www.codeeval.com/open_challenges/1/

import sys


def solution_plain(line):
    result = []
    x, y, n = map(int, line.split())
    for i in range(1, n + 1):
        fb = False
        if i % x == 0:
            fb = True
            result.append('F')
        if i % y == 0:
            fb = True
            result.append('B')
        if not fb:
            result.append(str(i))
        result.append(' ')

    return ''.join(result)


def solution(line):
    x, y, n = map(int, line.split())
    result = [
        (((i % x == 0) * 'F' + (i % y == 0) * 'B') or '%d' % i) + ' '
        for i in range(1, n + 1)
    ]
    return ''.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')