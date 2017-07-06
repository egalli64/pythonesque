"""
CodeEval Type Ahead
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/07/codeeval-type-ahead.html
      https://www.codeeval.com/open_challenges/55/
"""
import sys
from collections import defaultdict

TEXT = ['Mary', 'had', 'a', 'little', 'lamb', 'its', 'fleece', 'was',
        'white', 'as', 'snow', 'And', 'everywhere', 'that', 'Mary',
        'went', 'the', 'lamb', 'was', 'sure', 'to', 'go', 'It',
        'followed', 'her', 'to', 'school', 'one', 'day', 'which', 'was',
        'against', 'the', 'rule', 'It', 'made', 'the', 'children',
        'laugh', 'and', 'play', 'to', 'see', 'a', 'lamb', 'at', 'school',
        'And', 'so', 'the', 'teacher', 'turned', 'it', 'out', 'but',
        'still', 'it', 'lingered', 'near', 'And', 'waited', 'patiently',
        'about', 'till', 'Mary', 'did', 'appear', 'Why', 'does', 'the',
        'lamb', 'love', 'Mary', 'so', 'the', 'eager', 'children', 'cry',
        'Why', 'Mary', 'loves', 'the', 'lamb', 'you', 'know', 'the',
        'teacher', 'did', 'reply']

n_grams = {}


def check_n_grams(n):
    if n in n_grams:
        return

    item = defaultdict(lambda: defaultdict(int))
    for i in range(len(TEXT) - n):
        outer = ' '.join(TEXT[i:i + n])
        intern = TEXT[i + n]
        item[outer][intern] += 1

    n_grams[n] = item


def solution(n, given):
    n -= 1
    check_n_grams(n)

    target = n_grams[n][given]

    values = list(target.items())
    values.sort(key=lambda x: x[0])
    values.sort(key=lambda x: x[1], reverse=True)

    results = []
    population = sum(target.values())
    for value in values:
        results.append('{},{:.3f}'.format(value[0], value[1] / population))
    return ';'.join(results)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.split(',')
                print(solution(int(lhs), rhs.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
