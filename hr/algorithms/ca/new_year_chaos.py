"""
HackerRank Algorithms Constructive Algorithms New Year Chaos
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/new-year-chaos/problem

Given a shuffled list of the first n integers
Return the minum number of moves to get there from the natural order
 or -1 if more than 2 moves should be done for at least an element
"""
MAX_MOVES = 2


def solution(data):
    result = 0
    for i in reversed(range(len(data))):
        if data[i] > i + MAX_MOVES + 1:
            return -1

        for bribed in data[max(0, data[i] - MAX_MOVES):i]:
            if bribed > data[i]:
                result += 1

    return result


if __name__ == '__main__':
    for _ in range(int(input())):
        input() # data len, discarded
        data = list(map(int, input().split()))
        count = solution(data)
        print('Too chaotic' if count < 0 else count)
