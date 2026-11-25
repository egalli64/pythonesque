"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Greedy Algorithms
Money Change
Assume that you have an unlimited number of coins with denominations 1, 3, 9, and 27.
What is the minimum number of coins needed to change 100?
"""
DENOMINATIONS = [27, 9, 3, 1]  # safe choice, keeping bigger to smaller order


def solution(total: int) -> int:
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
    print(solution(100))
