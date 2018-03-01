"""
Closest Elements

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - divide and conquer

Given [870, 695, 790, 170, 918, 932, 539, 802, 648, 362, 770, 884, 377, 424, 845]
Compute the smallest absolute difference between two of its elements.
"""


def solution(values):
    result = float('inf')
    values.sort()

    for i in range(len(values) - 1):
        result = min(result, values[i+1] - values[i])
    return result


if __name__ == '__main__':
    print(solution([870, 695, 790, 170, 918, 932, 539, 802, 648, 362, 770, 884, 377, 424, 845]))
