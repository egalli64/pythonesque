"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
monkey_trouble https://codingbat.com/prob/p120546
"""
from monkey_trouble import monkey_trouble


class TestMonkeyTrouble:
    def test_given_1(self):
        assert monkey_trouble(True, True) is True

    def test_given_2(self):
        assert monkey_trouble(False, False) is True

    def test_given_3(self):
        assert monkey_trouble(True, False) is False
