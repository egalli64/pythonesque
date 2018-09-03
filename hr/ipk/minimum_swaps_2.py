"""
HackerRank  Interview Preparation Kit  Arrays  Minimum Swaps 2
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/minimum-swaps-2/problem

Given an unordered array of consecutive integers in [1..n]
Return the minimum number of swaps to sort it in natural order
"""


def solution(values):
    result = 0

    for i in range(len(values)-1):
        while values[i] != i+1:
            # silliness in a test case makes code weirder than necessary
            tmp = len(values) if values[i] > len(values) else values[i]
            values[i] = values[tmp-1]
            values[tmp-1] = tmp

            result += 1

    return result


if __name__ == '__main__':
    input()  # skip header
    data = list(map(int, input().split()))
    print(solution(data))
