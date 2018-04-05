"""
HackerRank Algorithms Implementation Drawing Book

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/drawing-book/problem

Given two integers, n and p,
representing the number of pages in a book and the page we have to reach

Return the minum number of pages we have to turn
"""


def solution(last, target):
    return min(target // 2, last // 2 - target // 2)


if __name__ == '__main__':
    n = int(input())
    p = int(input())

    print(solution(n, p))