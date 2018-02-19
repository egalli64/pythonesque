"""
Binary Search

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""


def solution(data, targets):
    results = []

    for target in targets:
        left = 0
        right = len(data) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if data[middle] == target:
                results.append(middle)
                break
            elif data[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        else:
            results.append(-1)

    return results


if __name__ == '__main__':
    l_dummy, *lhs = [int(x) for x in input().split()]
    r_dummy, *rhs = [int(x) for x in input().split()]

    print(' '.join([str(x) for x in solution(lhs, rhs)]))
