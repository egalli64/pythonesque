"""
CodeEval Python JSON Menu IDs
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/102/
"""
import sys
import json


def solution(line):
    doc = json.loads(line)
    return sum(elem['id'] for elem in doc["menu"]["items"] if elem is not None and "label" in elem)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test))
    else:
        print('Data filename expected as argument!')
