"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
common_end: https://codingbat.com/prob/p147755
"""
from common_end import common_end


class TestCommonEnd:
    """assuming pytest"""

    def test_given_1(self):
        assert common_end([1, 2, 3], [7, 3]) is True

    def test_given_2(self):
        assert common_end([1, 2, 3], [7, 3, 2]) is False

    def test_given_3(self):
        assert common_end([1, 2, 3], [1, 3]) is True
