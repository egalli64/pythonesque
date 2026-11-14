"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Check if a sequence contains a majority element.
Boyer-Moore Voting Algorithm
"""


def solution(xs: list[int]) -> bool:
    """Linear time, constant space"""
    if not xs:
        return False

    result = xs[0]
    count = 0

    # Wrong candidates would be obliterated by the other ones.
    # If a candidate as the majority vote can't be popped out.
    for x in xs:
        if count == 0:
            result = x
            count = 1
        elif x == result:
            count += 1
        else:
            count -= 1

    # Ensure the result is actually a majority
    return xs.count(result) > len(xs) // 2
