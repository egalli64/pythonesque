"""
Find the highest score
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-find-highest-score.html
      https://www.codeeval.com/open_challenges/208/
"""
import sys


def solution(line):
    authors = [[int(score) for score in author.split()] for author in line.split('|')]
    styles = zip(*authors)
    result = map(max, styles)
    return ' '.join(map(str, result))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')