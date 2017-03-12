"""
CodeEval Ugly Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/42/
"""
import sys


def is_ugly(number):
    return number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0


def split(line):
    result = [int(line)]
    for i in range(1, len(line)):
        lhs = line[:i]
        left = int(lhs)
        others = split(line[i:])
        for j in range(len(others)):
            result.append(left + others[j])
            result.append(left - others[j])
    return result


def solution(line):
    numbers = split(line)
    result = 0
    for number in numbers:
        if is_ugly(number):
            result += 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
