"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_splosion https://codingbat.com/prob/p118366
"""


def string_splosion(str):
    """
    Parameters:
        str a non-empty string
    Return a concatenation of all the substrings of str from a single char to the full string
    """
    result = ""
    for i in range(len(str)):
        result += str[: i + 1]
    return result
