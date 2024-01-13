"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
sleep_in https://codingbat.com/prob/p173401
"""


def sleep_in(weekday, vacation):
    """
    Parameters:
        weekday boolean
        vacation boolean
    return True if it is not a weekday or we're on vacation
    """
    return not weekday or vacation
