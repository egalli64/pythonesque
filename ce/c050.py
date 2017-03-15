"""
CodeEval String Substitution
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/50/
"""
import sys


def solution(line):
    data, changes = line.split(';')
    changes = changes.split(',')
    shadow = data

    for sub, enter in zip(changes[0::2], changes[1::2]):
        while True:
            pos = shadow.find(sub)
            if pos == -1:
                break
            hole = '_' * len(enter)
            shadow = shadow[:pos] + hole + shadow[pos+len(sub):]
            data = data[:pos] + enter + data[pos+len(sub):]
    return data

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
