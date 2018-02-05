"""
Trick or Treat
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-trick-or-treat.html
      https://www.codeeval.com/open_challenges/220/
"""

import sys


def solution(line):
    vampires, zombies, witches, houses = [int(item.split(': ')[1]) for item in line.split(',')]
    candies = (vampires * 3 + zombies * 4 + witches * 5) * houses
    return candies // (vampires + zombies + witches)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')