"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Last Digit of the Sum of the first n Fibonacci Numbers
Fast solution based on:
- Pisano (base 10) period
- Noting that sum of fibonacci in [0...n] == fib(n+2) - 1
"""
PISANO = 60


def solution(n: int) -> int:
    if n <= 1:
        return n

    n %= PISANO

    previous = 0
    current = 1
    for _ in range(n + 1):
        previous, current = current, (previous + current) % 10

    return (current - 1) % 10
