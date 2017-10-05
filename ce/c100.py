"""
CodeEval Python Even Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/100/
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(1 if int(test) % 2 == 0 else 0)
    else:
        print('Data filename expected as argument!')
