"""
HackerRank Algorithms Implementation Bon Appétit

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/bon-appetit/problem

Given
- two integers, n and k
- a list of integers c
- an integer, b

Return
- 'Bon Appetit' if b equals the sum of c minus its k element
- their difference otherwise
"""


def solution(gap, data, total):
    expected = (sum(data) - data[gap]) // 2
    if expected == total:
        return 'Bon Appetit'
    return total - expected


if __name__ == '__main__':
    _, k = map(int, input().split())
    c = list(map(int, input().split()))
    b = int(input())

    print(solution(k, c, b))