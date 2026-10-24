"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
pos_neg https://codingbat.com/prob/p162058
"""
from pos_neg import pos_neg


class TestPosNeg:
    def test_given_1(self):
        assert pos_neg(1, -1, False) is True

    def test_given_2(self):
        assert pos_neg(-1, 1, False) is True

    def test_given_3(self):
        assert pos_neg(-4, -5, True) is True
