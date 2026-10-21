"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
has23: https://codingbat.com/prob/p177892
"""
from has23 import has23


class TestHas23:
    """assuming pytest"""

    def test_given_1(self):
        assert has23([2, 5]) is True

    def test_given_2(self):
        assert has23([4, 3]) is True

    def test_given_3(self):
        assert has23([4, 5]) is False
