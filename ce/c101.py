"""
CodeEval Python Find A Square
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/101/
"""
import sys
import ast


def solution(line):
    vertices = ast.literal_eval(line)
    vertices = sorted(vertices)
    a = (vertices[0][0] - vertices[1][0]) ** 2 + (vertices[0][1] - vertices[1][1]) ** 2
    b = (vertices[0][0] - vertices[2][0]) ** 2 + (vertices[0][1] - vertices[2][1]) ** 2
    c = (vertices[2][0] - vertices[3][0]) ** 2 + (vertices[2][1] - vertices[3][1]) ** 2
    d = (vertices[2][0] - vertices[3][0]) ** 2 + (vertices[2][1] - vertices[3][1]) ** 2
    if a == 0 or a != b or a != c or a != d:
        return False

    diagonal = (vertices[1][0] - vertices[2][0]) ** 2 + (vertices[1][1] - vertices[2][1]) ** 2
    return True if diagonal == a + b else False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print('true' if solution(test) else 'false')
    else:
        print('Data filename expected as argument!')
