"""
CodeEval Overlapping Rectangles
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/70/
"""
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = map(int, test.split(','))
                print(ax1 <= bx2 and ax2 >= bx1 and ay1 >= by2 and ay2 <= by1)
    else:
        print('Data filename expected as argument!')
