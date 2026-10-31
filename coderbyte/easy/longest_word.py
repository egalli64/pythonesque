"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Longest Word
"""
import re


def longest_word(s: str):
    """
    Extract the "words" (letter and numbers) from the input string and return the longest one.
    Assume the input string is not empty, in case of same-length longest strings, return the first one.
    """
    words = re.findall(r"[a-zA-Z0-9]+", s)
    words.sort(key=len, reverse=True)
    return words[0]


print(longest_word("Hello world123 567"))
