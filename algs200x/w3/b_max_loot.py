"""
Maximizing the Value of a Loot

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""


def solution(capacity, items):
    result = 0.0
    loot = sorted(items, key= lambda item: item[0]/item[1])

    available = capacity
    while loot and available > 0:
        current = loot[-1][1] if loot[-1][1] < available else available
        result += loot[-1][0] / loot[-1][1] * current
        available -= current
        loot.pop()

    return result


if __name__ == '__main__':
    n, size = map(int, input().split())

    values = []
    for i in range(n):
        value, weight = map(int, input().split())
        values.append((value, weight))

    print('{:.4f}'.format(solution(size, values)))
