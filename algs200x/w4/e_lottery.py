"""
Organizing a Lottery

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""


def solution_sort(segments, points):
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


def solution_naive(segments, points):
    results = []

    for point in points:
        result = 0
        for segment in segments:
            if segment[0] <= point <= segment[1]:
                result += 1
        results.append(result)

    return results


if __name__ == '__main__':
    s, p = map(int, input().split())

    a = []
    for i in range(s):
        lhs, rhs = map(int, input().split())
        a.append((lhs, rhs))

    b = [int(x) for x in input().split()]

    items = solution_sort(a, b)
    print(' '.join(str(x) for x in items))
    print(sum(items))
