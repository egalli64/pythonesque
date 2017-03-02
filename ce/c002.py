"""
Longest Lines
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-longest-lines.html
      https://www.codeeval.com/open_challenges/2/
"""

import sys


def solution(size, lines):
    lines.sort(key=len, reverse=True)
    del lines[size:]
    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = open(sys.argv[1], 'r')
        top = int(data.readline())
        lines = [line.rstrip('\n') for line in data]
        data.close()

        print(solution(top, lines))
    else:
        print('Data filename expected as argument!')