"""
HackerRank Algorithms Implementation Find Digits

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/find-digits/problem

Given a number, count how many of its ciphers are also its divisor.
"""


def solution(data):
    result = 0

    value = int(data)
    for c in data:
        i = int(c)
        if i == 0:
            continue
        if value % i == 0:
            result += 1
    
    return result


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solution(input()))
