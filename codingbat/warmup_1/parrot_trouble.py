"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
parrot_trouble https://codingbat.com/prob/p166884
"""


def parrot_trouble(talking, hour):
    """
    Parameters:
        talking boolean
        hour number in [0 .. 23]
    return true if the parrot is talking and the hour is before 7 or after 20
    """
    return talking and (hour < 7 or hour > 20)
