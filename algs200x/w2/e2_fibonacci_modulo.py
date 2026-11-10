"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Fibonacci modulo m
Smarter solution by Pisano
"""


def pisano(modulo: int) -> int:
    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):
        buffer = (previous + current) % modulo
        previous = current
        current = buffer

        result += 1

    return result


def fibonacci(n: int, modulo: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % modulo

    return current


def solution(number: int, modulo: int) -> int:
    return fibonacci(number % pisano(modulo), modulo)
