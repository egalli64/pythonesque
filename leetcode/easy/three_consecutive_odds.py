"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1550. Three Consecutive Odds: https://leetcode.com/problems/three-consecutive-odds/description/
"""

from typing import List


def threeConsecutiveOdds(arr: List[int]) -> bool:
    i = 0
    while i < len(arr) - 2:
        for _ in range(3):
            if arr[i] % 2 == 0:
                break
            else:
                i += 1
        else:
            return True
        i += 1
    return False
