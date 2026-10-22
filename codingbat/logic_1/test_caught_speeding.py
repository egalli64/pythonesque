"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
caught_speeding: https://codingbat.com/prob/p137202
"""
from caught_speeding import caught_speeding


class TestCaughtSpeeding:
    """assuming pytest"""

    def test_given_1(self):
        assert caught_speeding(60, False) == 0

    def test_given_2(self):
        assert caught_speeding(65, False) == 1

    def test_given_3(self):
        assert caught_speeding(65, True) == 0
