"""
CodeEval Multiplication Tables
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/23/
"""
for i in range(1, 13):
    for j in range(1, 13):
        print('{:4}'.format(i*j), end='')
    print()
