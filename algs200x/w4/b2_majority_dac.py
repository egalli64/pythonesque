"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Check if a sequence contains a majority element.
Divide and Conquer
"""


def solution(data: list[int]) -> bool:
    """Divide and Conquer approach - n log n"""

    def majority(left: int, right: int) -> int | None:
        size = right - left + 1
        if size == 1:
            return data[left]
        if size == 2:
            return data[left] if data[left] == data[right] else None

        mid = (left + right) // 2
        lhs = majority(left, mid)
        rhs = majority(mid + 1, right)

        if lhs == rhs:
            return lhs
        # no agreement, check both candidates
        for candidate in (lhs, rhs):
            if candidate is not None:
                count = 0
                for i in range(left, right + 1):
                    if data[i] == candidate:
                        count += 1
                if count > size // 2:
                    return candidate
        return None

    if not data:
        return False
    return True if majority(0, len(data) - 1) else False
