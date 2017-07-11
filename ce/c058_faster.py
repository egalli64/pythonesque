"""
CodeEval Levenshtein Distance - Faster implementation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/58/
"""
import sys
from collections import deque

words = set()


def is_swap(lhs, rhs):
    difference = False
    for left, right in zip(lhs, rhs):
        if left != right:
            if difference:
                return False
            difference = True
    return difference


def is_add(shorter, longer):
    if len(shorter) > len(longer):
        shorter, longer = longer, shorter

    x = 0
    i = 0
    while i < len(shorter):
        if shorter[i] != longer[i+x]:
            if x == 1:
                return False
            x += 1
        else:
            i += 1

    return True if x < 2 else False


def get_friends(item):
    result = []
    for word in words:
        if (len(item) == len(word) and is_swap(item, word) or
                abs(len(item) - len(word)) == 1 and is_add(item, word)):
            result.append(word)
    return result


def solution(word):
    results = []
    visited = set()

    net = deque()
    if word not in words:
        return 0
    net.append(word)
    visited.add(word)

    while net:
        friend = net.popleft()
        fofs = get_friends(friend)
        for fof in fofs:
            if fof not in visited:
                net.append(fof)
                visited.add(fof)
        results.append(friend)

    return len(results)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Data filename expected as argument!')
        exit(0)

    tests = []
    with open(sys.argv[1], 'r') as file:
        for test in file:
            if test == 'END OF INPUT\n':
                break
            tests.append(test.rstrip('\n'))
        for test in file:
            words.add(test.rstrip('\n'))

    for test in tests:
        print(solution(test))
