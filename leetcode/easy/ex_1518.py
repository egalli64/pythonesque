"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1518. Water Bottles
https://leetcode.com/problems/water-bottles/description/
"""

def numWaterBottles(numBottles: int, numExchange: int) -> int:
    """
    Given a number of water bottles full of water, and knowing that you can
    exchange empty water bottles from the market with one full water bottle,
    return the maximum number of water bottles you can drink.

    Each (numExchange - 1) lot of bottles gives a free bottle.
    """
    return numBottles + (numBottles - 1) // (numExchange - 1)
