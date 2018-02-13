"""
Collecting Signatures

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""


def solution(segments):
    segments.sort(key=lambda item: item[1])

    results = [segments[0][1]]
    for segment in segments:
        if segment[0] > results[-1]:
            results.append(segment[1])

    return len(results), results


if __name__ == '__main__':
    n = int(input())

    items = []
    for i in range(n):
        lhs, rhs = map(int, input().split())
        items.append((lhs, rhs))

    print(solution(items))
