"""
HackerRank Algorithms Implementation Save the Prisoner!

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/save-the-prisoner/problem

Given a round robin distribution among n prisoners of m sweets starting from s position
Return who gets the last one. Warn! prisoner zero --> n!
"""


def solution(prisoners, sweets, begin):
    candidate = (sweets + begin - 1) % prisoners
    return candidate if candidate else prisoners


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m, s = map(int, input().split())
        print(solution(n, m, s))