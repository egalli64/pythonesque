"""
Faster Fibonacci calculator
"""


def calc_fib(n):
    if n <= 1:
        return n

    results = [1, 1]
    for _ in range(n - 2):
        results.append(results[-1] + results[-2])

    return results[-1]


print(calc_fib(int(input())))
