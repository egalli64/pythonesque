"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Improving Quick Sort
Step 1 - no improvement, classic Quick Sort
"""


def _quick(data: list[int], left: int, right: int) -> None:
    def partition(low: int, high: int) -> int:
        pivot_value = data[low]

        i = low
        j = high + 1

        while True:
            i += 1
            while data[i] < pivot_value:
                if i == high:
                    break
                i += 1

            j -= 1
            while data[j] > pivot_value:
                if j == low:
                    break
                j -= 1

            if i >= j:
                break
            data[i], data[j] = data[j], data[i]

        data[low], data[j] = data[j], data[low]
        return j

    if right <= left:
        return

    # call partition() to get a pivot, call recursively the function on the split interval
    pivot = partition(left, right)
    _quick(data, left, pivot - 1)
    _quick(data, pivot + 1, right)


def solution(data: list[int]):
    _quick(data, 0, len(data) - 1)
