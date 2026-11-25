"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Dynamic Programming
Money Change Again
"""
DENOMINATIONS = [1, 5, 6]


def solution_dp(target: int) -> int:
    assert DENOMINATIONS[0] == 1  # algorithm precondition
    cache = [0] * (target + 1)

    for i in range(1, target + 1):
        cache[i] = cache[i - 1] + 1
        for coin in DENOMINATIONS[1:]:
            if coin <= i:
                other = cache[i - coin] + 1
                cache[i] = min(cache[i], other)

    return cache[-1]


if __name__ == '__main__':
    print(solution_dp(28))
