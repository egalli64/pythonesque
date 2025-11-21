"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

1930. Unique Length-3 Palindromic Subsequences
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
"""

from typing import List


def countPalindromicSubsequence(s: str) -> int:
    """How many palindromes size 3 are in the input s?"""

    positions = {}

    for i, ch in enumerate(s):
        if ch not in positions:
            positions[ch] = [i, i]
        else:
            positions[ch][1] = i

    result = 0
    for first, last in positions.values():
        if last - first > 1:
            inside = set(s[first + 1:last])
            result += len(inside)

    return result


if __name__ == "__main__":
    """Smoke test"""
    print(countPalindromicSubsequence("aabca") == 3)
    print(countPalindromicSubsequence("adc") == 0)
    print(countPalindromicSubsequence("bbcbaba") == 4)

