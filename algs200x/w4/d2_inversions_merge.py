"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Number of Inversions
Based on merge sort algorithm
"""


def _merge_sort(data: list[int], left: int, right: int) -> int:
    def merge(low: int, middle: int, high: int) -> int:
        merged = []
        inversions = 0

        i = low
        j = middle + 1
        while i <= middle and j <= high:
            if data[i] > data[j]:
                inversions += middle - i + 1
                merged.append(data[j])
                j += 1
            else:
                merged.append(data[i])
                i += 1

        merged.extend(data[i:middle + 1])
        merged.extend(data[j:high + 1])

        data[low:high + 1] = merged
        return inversions

    # use merge sort to get as byproduct the number of inversions
    result = 0

    if left < right:
        pivot = left + (right - left) // 2
        result += _merge_sort(data, left, pivot)
        result += _merge_sort(data, pivot + 1, right)
        result += merge(left, pivot, right)

    return result


def solution(data: list[int]) -> int:
    return _merge_sort(data, 0, len(data) - 1)
