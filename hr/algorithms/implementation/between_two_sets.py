"""
HackerRank Algorithms Implementation Between Two Sets

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/between-two-sets/problem

Given two arrays of integers.
Return the number of integers such as:
- The elements of the first array are all factors of it
- It is a factor of all elements of the second array
"""


def solution(minors, majors):
    result = 0
    for candidate in range(max(minors), min(majors) + 1):
        if all(candidate % below == 0 for below in minors) and all(above % candidate == 0 for above in majors):
            result += 1
    return result


if __name__ == '__main__':
    input()  # discard header
    lhs = list(map(int, input().split()))
    rhs = list(map(int, input().split()))

    print(solution(lhs, rhs))