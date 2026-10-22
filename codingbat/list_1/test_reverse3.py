"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
reverse3: https://codingbat.com/prob/p192962
"""
from reverse3 import reverse3


class TestReverse3:
    """assuming pytest"""

    def test_given_1(self):
        assert reverse3([1, 2, 3]) == [3, 2, 1]

    def test_given_2(self):
        assert reverse3([5, 11, 9]) == [9, 11, 5]

    def test_given_3(self):
        assert reverse3([7, 0, 0]) == [0, 0, 7]
