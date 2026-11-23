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
"""


def solution(target: int) -> list[int]:
    cache = [0] * (target + 1)
    for i in range(1, len(cache)):
        cache[i] = cache[i - 1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)

    result = [1] * cache[-1]

    for i in range(1, cache[-1]):
        result[-i] = target
        if cache[target - 1] == cache[target] - 1:
            target -= 1
        elif target % 2 == 0 and (cache[target // 2] == cache[target] - 1):
            target //= 2
        else:  # target % 3 == 0 and (cache[target // 3] == cache[target] - 1):
            target //= 3

    return result
