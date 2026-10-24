"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
not_string https://codingbat.com/prob/p189441
"""
from not_string import not_string


class TestNotString:
    def test_given_1(self):
        assert not_string('candy') == 'not candy'

    def test_given_2(self):
        assert not_string('x') == 'not x'

    def test_given_3(self):
        assert not_string('not bad') == 'not bad'
