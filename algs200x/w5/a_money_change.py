"""
Money Change Again

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/money-change-again.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
DENOMINATIONS = [1, 3, 4]


# recursive approach
def solution_naive(target):
    if target == 0:
        return 0

    result = target  # assuming 1 is among the available denominations
    for coin in DENOMINATIONS:
        if target >= coin:
            tentative = solution_naive(target - coin) + 1
            result = min(result, tentative)

    return result


def solution_dp(target):
    cache = [0] * (target + 1)

    for i in range(1, target + 1):
        cache[i] = cache[i-1] + 1  # assuming DENOMINATIONS[0] == 1
        for coin in DENOMINATIONS[1:]:
            if coin <= i:
                other = cache[i-coin] + 1
                cache[i] = min(cache[i], other)

    return cache[-1]


if __name__ == '__main__':
    print(solution_naive(int(input())))
