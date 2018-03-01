"""
Covering points by segments

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - greedy algorithms

You are given ten points on a line, [1, 2, 3, 5, 7, 9, 10, 11, 13, 15]
You would like to cover them with the least number of segments of length three.
"""
SIZE = 3


def solution(points):
    result = 1
    current = points[0]

    for point in points:
        if current + SIZE < point:
            current = point
            result += 1
    return result


if __name__ == '__main__':
    print(solution([1, 2, 3, 5, 7, 9, 10, 11, 13, 15]))
