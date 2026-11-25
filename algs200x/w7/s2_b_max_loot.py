"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w7

Week 7 - Final Exam - Greedy Algorithms
Maximum Value of the Loot
A thief breaks into a spice shop and finds four pounds of saffron, three pounds of vanilla, and five pounds of cinnamon.
His backpack fits at most nine pounds, the prices of saffron, vanilla, and cinnamon are 5000, 200, and 10 per pound.
What is the most valuable loot?
"""


def solution(capacity: int, items: list[tuple[int, int]]) -> int:
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
