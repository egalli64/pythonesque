"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Organizing a Lottery
Given a list of segments and a list of points, say how many hits on the segments has each point
Using sort as helper - the result does not guarantee the values order!
"""


def solution(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    s_open = []
    s_close = []

    for segment in segments:
        s_open.append(segment[0])
        s_close.append(segment[1])

    s_open.sort()
    s_close.sort()
    points.sort()

    results = []
    count = 0
    oi = 0
    ci = 0
    size = len(segments)
    for point in points:
        while oi < size and s_open[oi] <= point:
            oi += 1
            count += 1
        while ci < size and s_close[ci] < point:
            ci += 1
            count -= 1
        results.append(count)

    return results


if __name__ == '__main__':
    s, p = map(int, input().split())

    a = []
    for i in range(s):
        lhs, rhs = map(int, input().split())
        a.append((lhs, rhs))

    b = [int(x) for x in input().split()]

    items = solution(a, b)
    print(' '.join(str(x) for x in items))
    print(sum(items))
