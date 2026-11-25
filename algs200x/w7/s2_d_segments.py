"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Greedy Algorithms
Covering segments by points
Given a list of horizontal segments.
Get the least possible number of vertical lines so that each segment is intersected by at least one line.
"""


def solution(segments: list[tuple[int, int]]) -> tuple[int, list[int]]:
    segments.sort(key=lambda item: item[1])

    results = [segments[0][1]]
    for segment in segments:
        if segment[0] > results[-1]:
            results.append(segment[1])

    return len(results), results


if __name__ == '__main__':
    items = [(2, 18), (5, 10), (2, 6), (21, 23), (5, 7), (14, 16), (10, 14), (10, 21), (4, 11), (8, 12), (17, 20)]
    print(solution(items))
