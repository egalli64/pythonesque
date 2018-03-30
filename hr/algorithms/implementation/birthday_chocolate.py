"""
HackerRank Algorithms Implementation Birthday Chocolate

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/the-birthday-bar/problem

Given
- a list of N integers
- day and month 
Return the number of chops from the list such as:
- size is month
- total is day
"""


def solution(data, day, month):
    result = 0

    partial_sum = sum(data[:month])
    if partial_sum == day:
        result += 1
    for i in range(0, len(data) - month):
        partial_sum -= data[i]
        partial_sum += data[i+month]
        if partial_sum == day:
            result += 1

    return result


if __name__ == '__main__':
    input()  # discard header
    items = list(map(int, input().split()))
    d, m = map(int, input().split())

    print(solution(items, d, m))