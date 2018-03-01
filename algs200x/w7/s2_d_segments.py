"""
Covering segments by points

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - greedy algorithms

You are given eleven horizontal segments.
[(2, 18), (5, 10), (2, 6), (21, 23), (5, 7), (14, 16), (10, 14), (10, 21), (4, 11), (8, 12), (17, 20)]
Get the least possible number of vertical lines so that each segment is intersected by at least one line.
"""


def solution(segments):
    segments.sort(key=lambda item: item[1])

    results = [segments[0][1]]
    for segment in segments:
        if segment[0] > results[-1]:
            results.append(segment[1])

    return len(results), results


if __name__ == '__main__':
    items = [(2, 18), (5, 10), (2, 6), (21, 23), (5, 7), (14, 16), (10, 14), (10, 21), (4, 11), (8, 12), (17, 20)]
    print(solution(items))
