"""
HackerRank Algorithms Implementation Utopian Tree

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/utopian-tree/problem

Given an integer
Return the size of the tree, starting from 1, alternatively doubling and increasing by 1
"""


def solution(cycles):
    result = 1

    for i in range(cycles):
        if i % 2:
            result += 1
        else:
            result *= 2
    return result


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solution(int(input())))
