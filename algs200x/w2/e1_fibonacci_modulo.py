"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Fibonacci modulo m
Naive solution
"""


def solution(number: int, modulo: int) -> int:
    """Calculate Fibonacci, then return its modulo."""
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
