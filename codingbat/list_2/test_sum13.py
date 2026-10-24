"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
sum13: https://codingbat.com/prob/p167025
"""
from sum13 import sum13


class TestCountEvens:
    def test_given_1(self):
        assert sum13([1, 2, 2, 1]) == 6

    def test_given_2(self):
        assert sum13([1, 1]) == 2

    def test_given_3(self):
        assert sum13([1, 2, 2, 1, 13]) == 6

    def test_empty(self):
        assert sum13([]) == 0
