"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_match https://codingbat.com/prob/p182414
"""


def string_match(a, b):
    """
    Parameters:
        a str
        b str
    Return the number of same sized 2 subsequences in the same place in a and b
    """
    end = min(len(a), len(b))

    count = 0
    for i in range(end - 1):
        if a[i : i + 2] == b[i : i + 2]:
            count += 1
    return count
