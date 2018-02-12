"""
Last Digit of the Sum of Fibonacci Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x


Using Pisano period and sum of fib in [0..n] == fib(n+2) - 1
"""
PISANO = 60


def solution(number):
    if number < 2:
        return number

    number %= PISANO

    results = [1, 1]
    for _ in range(number):
        results.append((results[-1] + results[-2]) % 10)

    return (results[-1] - 1) % 10


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
