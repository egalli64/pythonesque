"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Last Digit of the Partial Sum of n Fibonacci Numbers
Fast solution based on:
- Pisano (base 10) period
- Noting that sum of fibonacci in [0...n] == fib(n+2) - 1
"""
PISANO = 60


def solution(left: int, right: int) -> int:
    assert left <= right

    fib_mods = [0, 1]
    for _ in range(PISANO - 2):
        fib_mods.append((fib_mods[-1] + fib_mods[-2]) % 10)

    left %= PISANO
    right %= PISANO
    if right < left:
        right += PISANO

    result = 0
    for i in range(left, right + 1):
        result += fib_mods[i % PISANO]
    return result % 10
