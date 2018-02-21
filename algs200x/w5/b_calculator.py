"""
Primitive Calculator

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/primitive-calculator.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""


def solution_naive(target):
    results = [target]
    while results[-1] > 1:
        if results[-1] % 3 == 0:
            results.append(results[-1] // 3)
        elif results[-1] % 2 == 0:
            results.append(results[-1] // 2)
        else:
            results.append(results[-1] - 1)
    return results[::-1]


def solution_dp(target):
    cache = [0] * (target + 1)
    for i in range(1, len(cache)):
        cache[i] = cache[i-1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)

    result = [1] * cache[-1]
    for i in range(1, cache[-1]):
        result[-i] = target
        if cache[target-1] == cache[target] - 1:
            target -= 1
        elif target % 2 == 0 and (cache[target // 2] == cache[target] - 1):
            target //= 2
        else:  # target % 3 == 0 and (cache[target // 3] == cache[target] - 1):
            target //= 3
    return result
