"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
in1to10: https://codingbat.com/prob/p158497
"""
from in1to10 import in1to10


class TestIn1to10:
    """assuming pytest"""

    def test_given_1(self):
        assert in1to10(5, False) is True

    def test_given_2(self):
        assert in1to10(11, False) is False

    def test_given_3(self):
        assert in1to10(11, True) is True
