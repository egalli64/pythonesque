"""
CodeEval Python Lowest Unique Number
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/10/lowest-unique-number.html
      https://www.codeeval.com/open_challenges/103/
"""
import sys
from collections import Counter


def solution(line):
    data = [int(x) for x in line.split()]
    counter = Counter(data)
    for key, value in sorted(counter.items()):
        if  value == 1:
            return data.index(key) + 1
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test))
    else:
        print('Data filename expected as argument!')
