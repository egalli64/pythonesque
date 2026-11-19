"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Improving Quick Sort
Let it works fast even on sequences containing many equal elements
"""


def partition(data: list[int], left: int, right: int) -> int:
    pivot = data[left]

    i = left
    j = right + 1

    while True:
        i += 1
        while data[i] < pivot:
            if i == right:
                break
            i += 1

        j -= 1
        while data[j] > pivot:
            if j == left:
                break
            j -= 1

        if i >= j:
            break
        data[i], data[j] = data[j], data[i]

    data[left], data[j] = data[j], data[left]
    return j


def quick(data: list[int], left: int, right: int) -> None:
    if right <= left:
        return

    pivot = partition(data, left, right)
    quick(data, left, pivot - 1)
    quick(data, pivot + 1, right)


def solution_quick(data: list[int]):
    quick(data, 0, len(data) - 1)


def quick3(data: list[int], left: int, right: int) -> None:
    if right <= left:
        return

    p_left = left
    p_right = right
    pivot = data[left]
    i = left + 1
    while i <= p_right:
        if data[i] < pivot:
            data[p_left], data[i] = data[i], data[p_left]
            p_left += 1
            i += 1
        elif data[i] > pivot:
            data[p_right], data[i] = data[i], data[p_right]
            p_right -= 1
        else:
            i += 1

    quick3(data, left, p_left - 1)
    quick3(data, p_right + 1, right)


def solution_quick3(data: list[int]) -> None:
    quick3(data, 0, len(data) - 1)
