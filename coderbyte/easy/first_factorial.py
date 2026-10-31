"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

First Factorial
"""


def first_factorial(num: int) -> int:
    """
    Given an integer in [1...18], return its factorial.
    """
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


print(first_factorial(4))
