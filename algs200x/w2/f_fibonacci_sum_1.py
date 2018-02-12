"""
Last Digit of the Partial Sum of Fibonacci Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x

Naive solution
"""


def solution(beg, last):
    result = 0

    previous = 0
    current = 1

    for i in range(last + 1):
        if i >= beg:
            result += previous

        previous, current = current, previous + current

    return result % 10


if __name__ == '__main__':
    lhs, rhs = map(int, input().split())
    print(solution(lhs, rhs))