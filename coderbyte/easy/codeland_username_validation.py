"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Codeland Username Validation
"""
import re


def username_validation(s: str) -> str:
    """
    1. The username is between 4 and 25 characters.
    2. It must start with a letter.
    3. It can only contain letters, numbers, and the underscore character.
    4. It cannot end with an underscore character.

    Return the string "true" if the username is valid, otherwise return "false"
    """
    if len(s) < 4 or len(s) > 25:
        return "false"
    if not s[0].isalpha():
        return "false"
    if s[-1] == "_":
        return "false"
    for ch in s:
        if not ch.isalpha() and not ch.isdigit() and ch != "_":
            return "false"

    return "true"


def re_username_validation(s: str) -> str:
    return "true" if re.match(r"[a-zA-Z]\w{2,23}[a-zA-Z0-9]$", s) else "false"
