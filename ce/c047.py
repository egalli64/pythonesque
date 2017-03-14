"""
CodeEval Palindromic Ranges
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/47/
"""
import sys


def is_palindrome(number):
    if number < 10:
        return True
    if number < 100:
        return True if number // 10 == number % 10 else False
    if number < 1000:
        return True if number // 100 == number % 10 else False
    return False


def is_interesting(beg, end):
    palindromes = 0
    for i in range(beg, end+1):
        if is_palindrome(i):
            palindromes += 1
    return not (palindromes % 2)


def solution(line):
    beg, end = map(int, line.split())
    result = 0
    for i in range(beg, end+1):
        for j in range(i, end+1):
            if is_interesting(i, j):
                result += 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
