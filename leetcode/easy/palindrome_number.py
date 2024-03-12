"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

9. Palindrome Number: https://leetcode.com/problems/palindrome-number/description/
"""


def isPalindrome(x: int) -> bool:
    """
    Given an integer in [-2^31 .. 2^31] check if it is a palindrome
    """
    if x < 0:
        return False
    if x < 10:
        return True
    if x % 10 == 0:
        return False
    
    other_half = 0
    while x > other_half:
        other_half = other_half * 10 + x % 10
        x //= 10
    
    return x == other_half or x == other_half // 10
