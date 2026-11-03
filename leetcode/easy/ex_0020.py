"""
LeetCode: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

20. Valid Parentheses
"""


def is_valid(s: str) -> bool:
    """
    Given a string s containing just '(', ')', '{', '}', '[' and ']', check if it is valid.
    The parentheses should match.
    """
    stack = []

    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        elif not stack:
            return False
        else:
            match stack.pop():
                case '(':
                    if ch != ')':
                        return False
                case '[':
                    if ch != ']':
                        return False
                case '{':
                    if ch != '}':
                        return False
                case _:
                    return False

    return not stack
