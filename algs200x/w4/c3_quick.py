"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Improving Quick Sort: implementing 3 way partitions
Let it works fast even on sequences containing many equal elements
"""


def _quick(data: list[int], left: int, right: int) -> None:
    if right <= left:
        return

    p_left = left
    p_right = right
    pivot_value = data[left]
    i = left + 1
    while i <= p_right:
        if data[i] < pivot_value:
            data[p_left], data[i] = data[i], data[p_left]
            p_left += 1
            i += 1
        elif data[i] > pivot_value:
            data[p_right], data[i] = data[i], data[p_right]
            p_right -= 1
        else:
            i += 1

    _quick(data, left, p_left - 1)
    _quick(data, p_right + 1, right)


def solution(data: list[int]) -> None:
    _quick(data, 0, len(data) - 1)
