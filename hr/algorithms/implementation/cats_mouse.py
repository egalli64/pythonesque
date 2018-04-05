"""
HackerRank Algorithms Implementation Cats and a Mouse

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

Given a list of integers, representing the positions on a line for
- cat A, cat B, mouse C

Return which cat reaches the mouse first, or mouse in case of tie
"""


def solution(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    if a == b:
        return 'Mouse C'
    return 'Cat A' if a < b else 'Cat B'


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solution(*list(map(int, input().split()))))
