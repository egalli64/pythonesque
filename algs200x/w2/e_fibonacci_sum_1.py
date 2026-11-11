"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Last Digit of the Sum of Fibonacci Numbers
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
