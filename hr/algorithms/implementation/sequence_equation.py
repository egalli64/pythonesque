"""
HackerRank Algorithms Implementation Sequence Equation

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/permutation-equation/problem

Given a list of integers
Return it after applying this transformation:
The element at position x is the value of the element at position x-1 in the original list

Ex: [5, 2, 1, 3, 4] -> [4, 2, 5, 1, 3]
    [2, 3, 1] -> [2, 3, 1]
"""


def solution(items):
    buffer = [0] * len(items)
    for i in range(len(items)):
        buffer[items[i]-1] = i+1

    result = []
    for i in range(len(buffer)):
        result.append(buffer[buffer[i]-1])

    return result


if __name__ == '__main__':
    input()  # unused
    data = list(map(int, input().split()))
    print('\n'.join(map(str, solution(data))))
