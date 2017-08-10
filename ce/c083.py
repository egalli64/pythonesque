"""
CodeEval Beautiful Strings
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/83/
"""
import sys


def solution(line):
    counters = [0] * 26
    for c in line:
        if c.isalpha():
            i = ord(c.lower()) - ord('a')
            counters[i] += 1
    counters.sort(reverse=True)

    result = 0
    weight = 26
    for i in counters:
        if not i:
            break
        result += i * weight
        weight -= 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test))
    else:
        print('Data filename expected as argument!')
