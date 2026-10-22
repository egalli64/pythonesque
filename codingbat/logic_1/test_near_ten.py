"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
near_ten: https://codingbat.com/prob/p165321
"""
from near_ten import near_ten


class TestNearTen:
    """assuming pytest"""

    def test_given_1(self):
        assert near_ten(12) is True

    def test_given_2(self):
        assert near_ten(17) is False

    def test_given_3(self):
        assert near_ten(19) is True
