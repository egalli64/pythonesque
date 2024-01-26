"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
lucky_sum: https://codingbat.com/prob/p107863
"""


def lucky_sum(a, b, c):
    """
    Parameters:
        a int
        b int
        c int
    return the sum of parameters, excluding 13 and the values following it
    """
    result = 0
    if a == 13:
        return result
    else:
        result += a

    if b == 13:
        return result
    else:
        result += b

    if c != 13:
        result += c

    return result


def lucky_sum_alt(a, b, c):
    """
    Alternative solution

    Parameters:
        a int
        b int
        c int
    return the sum of parameters, excluding 13 and the values following it
    """
    result = a if a != 13 else 0
    result += b if a != 13 and b != 13 else 0
    result += c if a != 13 and b != 13 and c != 13 else 0

    return result
