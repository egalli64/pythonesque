"""
CodeEval Reverse And Add
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/45/
"""
import sys


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True


def solution(line):
    count = 0

    while True:
        count += 1
        current = int(line) + int(line[::-1])
        line = str(current)
        if is_palindrome(line):
            return '{} {}'.format(count, current)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
