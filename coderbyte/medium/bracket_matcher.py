"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Bracket Matcher
"""


def bracket_matcher(s: str) -> int:
    """Check if bracket matches given string"""
    brackets = []
    for c in s:
        if c == '(':
            brackets.append(c)
        elif c == ')':
            if not brackets or brackets[-1] == ')':
                return 0
            else:
                brackets.pop()

    return 0 if brackets else 1
