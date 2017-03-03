"""
CodeEval Lowercase
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/20/
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(test.rstrip('\n').lower())
        test_cases.close()
    else:
        print('Data filename expected as argument!')
