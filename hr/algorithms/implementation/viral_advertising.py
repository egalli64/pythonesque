"""
HackerRank Algorithms Implementation Viral Advertising

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/strange-advertising/problem


Given number of days in [1..50]
Return the like received, assuming that:
- on day 1, 5 people see the ad.
- each day half new shares like and share it to other 3 people

Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24
"""


def solution(days):
    shared = 5
    result = 0
    for _ in range(days):
        shared //= 2
        result += shared
        shared *= 3
    return result


if __name__ == '__main__':
    print(solution(int(input())))
