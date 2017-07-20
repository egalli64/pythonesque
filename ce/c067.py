"""
CodeEval Hex To Decimal
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenges/67/
      https://www.codeeval.com/
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(int(test.rstrip(), 16))
    else:
        print('Data filename expected as argument!')
