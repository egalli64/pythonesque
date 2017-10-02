"""
CodeEval Penultimate Word
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/92/
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(test.split()[-2])
    else:
        print('Data filename expected as argument!')
