"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Primitive Calculator
Compute the minimum number of operations needed to obtain the number n starting from the number 1.
The only operations available are:
- multiply x by 2
- multiply x by 3
- add 1 to x
Greedy approach would fail, we need backtracking!
"""


def solution(target: int) -> list[int]:
    result = [target]

    while result[-1] > 1:
        if result[-1] % 3 == 0:
            result.append(result[-1] // 3)
        elif result[-1] % 2 == 0:
            result.append(result[-1] // 2)
        else:
            result.append(result[-1] - 1)

    return result[::-1]
