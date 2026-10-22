"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
sorta_sum: https://codingbat.com/prob/p116620
"""
from sorta_sum import sorta_sum


class TestSortaSum:
    """assuming pytest"""

    def test_given_1(self):
        assert sorta_sum(3, 4) == 7

    def test_given_2(self):
        assert sorta_sum(9, 4) == 20

    def test_given_3(self):
        assert sorta_sum(10, 11) == 21
