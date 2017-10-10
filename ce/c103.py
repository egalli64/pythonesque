"""
CodeEval Python Lowest Unique Number
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/10/lowest-unique-number.html
      https://www.codeeval.com/open_challenges/103/
"""
import sys

NOT_FOUND = 0
FOUND_MANY = -1


def solution(line):
    data = [int(x) for x in line.split()]
    result = [NOT_FOUND] * 9
    for i, number in enumerate(data):
        result[number-1] = i+1 if result[number-1] == NOT_FOUND else FOUND_MANY

    for index in result:
        if index > NOT_FOUND:
            return index
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test))
    else:
        print('Data filename expected as argument!')
