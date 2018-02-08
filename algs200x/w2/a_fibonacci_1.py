"""
Naive Fibonacci calculator
Make some sort of sense only for very low input
"""


def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


print(calc_fib(int(input())))
