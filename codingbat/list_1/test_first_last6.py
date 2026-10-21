"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
first_last6: https://codingbat.com/prob/p181624
"""
from first_last6 import first_last6


class TestFirstLast6:
    """assuming pytest"""

    def test_given_1(self):
        assert first_last6([1, 2, 6]) is True

    def test_given_2(self):
        assert first_last6([6, 1, 2, 3]) is True

    def test_given_3(self):
        assert first_last6([13, 6, 1, 2, 3]) is False
