"""
Justify the Text
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/177/
"""

import sys


def solution(text):
    result = []
    while len(text) > 80:
        pos = 0
        while True:
            next_pos = text.find(' ', pos + 1)
            if next_pos == -1 or next_pos > 80:
                break
            pos = next_pos
        line = text[0:pos]

        words = line.split()
        blanks = 80 - len(line) + len(words)
        size = (blanks // (len(words) - 1))
        extra = blanks % (len(words) - 1) - 1
        for i in range(extra):
            words[i] += ' '
        result.append((' ' * size).join(words))

        text = text[pos + 1:]

    if text:
        result.append(text)
    return '\n'.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')