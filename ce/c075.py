"""
CodeEval Flavius Josephus
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/75/
"""
import sys


def solution(size, step):
    assert step < size
    results = []
    people = [str(x) for x in range(size)]

    kill = step-1
    for _ in range(size-1):
        results.append(people.pop(kill))
        kill = (kill + step - 1) % len(people)
    results.append(people[0])

    return ' '.join(results)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = map(int, test.split(','))
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
