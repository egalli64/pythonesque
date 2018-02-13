"""
Changing Money

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/half-dozen-of-greedy-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
DENOMINATIONS = [10, 5, 1]  # safe choice, keeping bigger to smaller order


def solution(total):
    leftover = total
    result = 0

    for coin in DENOMINATIONS:
        counter = leftover // coin
        if counter > 0:
            result += counter
            leftover %= coin

        if leftover == 0:
            break

    return result


if __name__ == '__main__':
    print(solution(int(input())))
