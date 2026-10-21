"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
sorta_sum: https://codingbat.com/prob/p116620
"""


def sorta_sum(a: int, b: int) -> int:
    """
    Parameters:
        a int
        b int
    return the parameters sum, but if it is in [10..19] then 20
    """
    candidate_result = a + b
    return 20 if 10 <= candidate_result <= 19 else candidate_result
