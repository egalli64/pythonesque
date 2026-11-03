"""
LeetCode: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

412. Fizz Buzz: https://leetcode.com/problems/fizz-buzz/
"""


def fizz_buzz(n: int) -> list[str]:
    """
    Generate fizz buzz sequence

    Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5
    """
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result
