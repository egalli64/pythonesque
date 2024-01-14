"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
near_hundred https://codingbat.com/prob/p124676
"""


def near_hundred(n):
    """
    Parameter:
        n int
    return true if n within 10 of 100 or 200
    """
    return abs(100 - n) <= 10 or abs(200 - n) <= 10
