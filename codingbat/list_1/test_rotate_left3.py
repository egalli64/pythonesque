"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
rotate_left3: https://codingbat.com/prob/p148661
"""
from rotate_left3 import rotate_left3


class TestRotateLeft3:
    """assuming pytest"""

    def test_given_1(self):
        assert rotate_left3([1, 2, 3]) == [2, 3, 1]

    def test_given_2(self):
        assert rotate_left3([5, 11, 9]) == [11, 9, 5]

    def test_given_3(self):
        assert rotate_left3([7, 0, 0]) == [0, 0, 7]
