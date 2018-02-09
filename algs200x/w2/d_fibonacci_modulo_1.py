"""
Calculate Fibonacci modulo m

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/fibonacci-modulo-with-pisano-period.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x

Naive solution
"""


def solution(number, modulo):
    if number < 2:
        return number

    previous = 0
    current = 1

    for _ in range(number - 1):
        previous, current = current, previous + current

    return current % modulo


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solution(n, m))
