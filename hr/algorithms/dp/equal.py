"""
HackerRank Algorithms Dynamic Programming Equal

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-equal.html
      https://www.hackerrank.com/challenges/equal/problem

Given a list of k integers, we have to make all equal adding n times 1, 2, or 5 to all but one item
Return the minimal n to equalize them
"""
SHIFT = [0, 1, 2]


def solution(data):
    lowest = min(data)

    results = [0] * len(SHIFT)
    for item in data:
        for i in SHIFT:
            gap = item - lowest + i
            results[i] += gap // 5 + SHIFT[(gap%5 + 1) // 2]
    return min(results)


if __name__ == '__main__':
    for _ in range(int(input())):
        input()  # discarded
        items = list(map(int, input().split()))

        print(solution(items))
