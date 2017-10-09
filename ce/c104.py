"""
CodeEval Python Word To Digit
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/104/
"""
import sys

MAP = {'zero' : '0', 'one' : '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
       'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def solution(line):
    numbers = line.split(';')
    result = []
    for number in numbers:
        result.append(MAP[number])
    return ''.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
