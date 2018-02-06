# Smarter last digit of a Fibonacci number calculator
import sys


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    print(get_fibonacci_last_digit(int(input())))
