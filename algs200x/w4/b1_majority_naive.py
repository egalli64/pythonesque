"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Check if a sequence contains a majority element.
"""


def solution(data: list[int]) -> bool:
    """Quadratic Algorithm"""
    checked = set()  # keep track of already checked elements
    size = len(data)

    # no need to check for an element that was not in the first half
    for i in range((size + 1) // 2):
        current = data[i]

        if current not in checked:
            checked.add(current)
            if data.count(current) > size // 2:
                return True

    return False
