"""
CodeEval N Mod M
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/62/
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                m, n = map(int, test.split(','))
                print(m - m//n * n)
    else:
        print('Data filename expected as argument!')
