"""
Maximum Value of the Loot

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - greedy algorithms

A thief breaks into a spice shop and finds four pounds of saffron, three pounds of vanilla, and five pounds of cinnamon.
His backpack fits at most nine pounds, the prices of saffron, vanilla, and cinnamon are 5000, 200, and 10 per pound.
What is the most valuable loot?
"""


def solution(capacity, items):
    result = 0

    available = capacity
    for item in items:
        current = item[1] if item[1] < available else available
        result += item[0] * current
        available -= current
        if not available:
            break

    return result


if __name__ == '__main__':
    print(solution(9, [(5000, 4), (200, 3), (10, 5)]))
