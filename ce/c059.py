"""
CodeEval Telephone Words
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/59/
"""
import sys

CODES = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi',
         '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def encode(number, root, index):
    if index == len(number):
        return [root]

    results = []
    for code in CODES[number[index]]:
        results.extend(encode(number, root + code, index + 1))
    return results


def solution(line):
    return ','.join(sorted(encode(line, '', 0)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
