"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
sum3: https://codingbat.com/prob/p191645
"""
from sum3 import sum3


class TestSum3:
    """assuming pytest"""

    def test_given_1(self):
        assert sum3([1, 2, 3]) == 6

    def test_given_2(self):
        assert sum3([5, 11, 2]) == 18

    def test_given_3(self):
        assert sum3([7, 0, 0]) == 7
