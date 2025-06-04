"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

3403. Find the Lexicographically Largest String From the Box I
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/
"""


def answerString(word: str, numFriends: int) -> str:
    """
    Find the "largest" substring after splitting the string between friends in all possible ways
    """
    if numFriends == 1:
        return word
    else:
        n = len(word) - numFriends + 1
        return max(word[i : i + n] for i in range(len(word)))
