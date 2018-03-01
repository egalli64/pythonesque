"""
Money Change Again

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/money-change-again.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - dynamic programming
"""
DENOMINATIONS = [1, 5, 6]


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
    print(solution_dp(28))
