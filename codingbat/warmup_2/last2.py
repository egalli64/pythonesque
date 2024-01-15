"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
last2 https://codingbat.com/prob/p145834
"""


def last2(str):
    """
    Parameters:
        str a non-empty string
    Return how many other times the last two chars of str as a substring is in str
    """
    tag = str[-2:]

    count = 0
    for i in range(len(str) - 2):
        if str[i] == tag[0] and str[i + 1] == tag[1]:
            count += 1

    return count


def last2_walrus(str):
    """
    Parameters:
        str a non-empty string
    Return how many other times the last two chars of str as a substring is in str
    """
    tag = str[-2:]

    count = 0
    i = 0
    while (i := str.find(tag, i) + 1) < len(str) - 2:
        count += 1

    return count
