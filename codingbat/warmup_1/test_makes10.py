"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
makes10 https://codingbat.com/prob/p124984
"""
from makes10 import makes10


class TestMakes10:
    def test_given_1(self):
        assert makes10(9, 10) is True

    def test_given_2(self):
        assert makes10(9, 9) is False

    def test_given_3(self):
        assert makes10(1, 9) is True
