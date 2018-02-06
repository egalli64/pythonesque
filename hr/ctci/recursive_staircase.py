"""
HackerRank Tutorials  Cracking the Coding Interview  Recursion: Davis' Staircase
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/hackerrank-recursion-davis-staircase.html
      https://www.hackerrank.com/challenges/ctci-recursive-staircase
"""
cache = [1, 2, 4]
MAX_STEPS = 36


def solution(steps):
    assert 0 < steps <= MAX_STEPS

    if steps <= len(cache):
        return cache[steps - 1]

    for _ in range(steps - len(cache)):
        cache.append(cache[-1] + cache[-2] + cache[-3])

    return cache[-1]


if __name__ == '__main__':
    number_of_stairs = int(input().strip())
    for _ in range(number_of_stairs):
        number_of_steps = int(input().strip())

        print(solution(number_of_steps))
