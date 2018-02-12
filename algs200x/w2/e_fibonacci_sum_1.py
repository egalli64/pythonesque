"""
Last Digit of the Sum of Fibonacci Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x

Naive solution
"""


def solution(n):
    if n < 2:
        return n

    previous = 0
    current = 1
    result = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        result += current

    return result % 10


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
