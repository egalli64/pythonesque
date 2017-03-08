"""
CodeEval Message Decoding
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-message-decoding.html
      https://www.codeeval.com/open_challenges/36/
"""
import sys


def key_generator():
    size = 1
    cur = 0
    while True:
        yield format(cur, '0{}b'.format(size))
        if cur == 2 ** size - 2:
            size += 1
            cur = 0
        else:
            cur += 1


def solution(line):
    mapping = {}
    i = 0
    for key in key_generator():
        if line[i] not in ['0', '1']:
            mapping[key] = line[i]
            i += 1
        else:
            break

    result = []
    while True:
        size = int(line[i:i + 3], 2)
        if size == 0:
            break
        i += 3
        while True:
            chunk = line[i:i+size]
            i += size
            if chunk not in mapping:
                break
            result.append(mapping[chunk])

    return ''.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')
