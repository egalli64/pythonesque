"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1550. Three Consecutive Odds: https://leetcode.com/problems/three-consecutive-odds/description/
"""


def three_consecutive_odds(arr: list[int]) -> bool:
    """Are there three consecutive odd numbers in the given array?"""
    i = 0
    while i < len(arr) - 2:
        triplet_count = 0
        for _ in range(3):
            if arr[i] % 2 != 0:
                i += 1
                triplet_count += 1
            else:
                break
        if triplet_count == 3:
            return True

        i += 1

    return False


def three_consecutive_odds_for_else(arr: list[int]) -> bool:
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
