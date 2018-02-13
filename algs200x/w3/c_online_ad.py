"""
Maximizing Revenue in Online Ad Placement

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/half-dozen-of-greedy-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""


def solution(profits, clicks):
    profits.sort()
    clicks.sort()

    result = 0
    for p, c in zip(profits, clicks):
        result += p * c

    return result


if __name__ == '__main__':
    input()  # header discarded

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(solution(a, b))
