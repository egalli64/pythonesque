"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
left2: https://codingbat.com/prob/p160545
"""


def left2(str):
    """
    Parameters:
        str having length 2+
    return rotate str, first two chars sent to the end
    """
    return str[2:] + str[:2]
