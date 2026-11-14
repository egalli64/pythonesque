"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Binary Search
Implement the binary search algorithm.
"""


def solution(data: list[int], targets: list[int]) -> list[int]:
    def binary_search(target: int) -> int:
        """
        Binary search

        Params:
            data: a sorted list of integers
            target: the searched element

        Returns:
            the target index, or -1 if missing.
        """
        left = 0
        right = len(data) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if data[middle] == target:
                return middle
            elif data[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    return [binary_search(target) for target in targets]


if __name__ == '__main__':
    l_dummy, *lhs = [int(x) for x in input().split()]
    r_dummy, *rhs = [int(x) for x in input().split()]

    print(' '.join([str(x) for x in solution(lhs, rhs)]))
