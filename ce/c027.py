"""
CodeEval Decimal to Binary
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/27/
"""
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print('{:b}'.format(int(test.rstrip('\n'))))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
