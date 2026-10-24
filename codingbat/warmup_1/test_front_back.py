"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
front_back https://codingbat.com/prob/p153599
"""
from front_back import front_back


class TestFrontBack:
    def test_given_1(self):
        assert front_back('code') == 'eodc'

    def test_given_2(self):
        assert front_back('a') == 'a'

    def test_given_3(self):
        assert front_back('ab') == 'ba'
