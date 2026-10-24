"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
near_hundred https://codingbat.com/prob/p124676
"""
from near_hundred import near_hundred


class TestNearHundred:
    def test_given_1(self):
        assert near_hundred(93) is True

    def test_given_2(self):
        assert near_hundred(90) is True

    def test_given_3(self):
        assert near_hundred(89) is False
