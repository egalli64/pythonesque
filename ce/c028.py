"""
CodeEval String Searching
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/28/
"""
import sys


def solution(line):
    string, pattern = line.split(',')

    if pattern == '*':
        return True

    pos = 0
    for c in string:
        if pattern[pos] == '*':
            if pos+1 == len(pattern):
                return True
            if c == pattern[pos+1]:
                pos += 2
                if pos >= len(pattern):
                    return True
            if c == '*' and pattern[pos+1] == '\\':
                pos += 3
                if pos >= len(pattern):
                    return True

        elif c == pattern[pos]:
            pos += 1
            if pos == len(pattern):
                return True

        elif c == '*' and pattern[pos] == '\\':
            pos += 2
            if pos >= len(pattern):
                return True

    return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print('true' if solution(test.rstrip('\n')) else 'false')
        test_cases.close()
    else:
        print('Data filename expected as argument!')
