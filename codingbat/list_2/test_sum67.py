"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
sum67: https://codingbat.com/prob/p108886
"""
from sum67 import sum67


class TestCountEvens:
    def test_given_1(self):
        assert sum67([1, 2, 2]) == 5

    def test_given_2(self):
        assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5

    def test_given_3(self):
        assert sum67([1, 1, 6, 7, 2]) == 4

    def test_extra_7(self):
        assert sum67([2, 2, 6, 7, 7]) == 11
