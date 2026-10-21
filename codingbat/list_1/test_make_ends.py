"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
make_ends: https://codingbat.com/prob/p124806
"""
from make_ends import make_ends


class TestMakeEnds:
    """assuming pytest"""

    def test_given_1(self):
        assert make_ends([1, 2, 3]) == [1, 3]

    def test_given_2(self):
        assert make_ends([1, 2, 3, 4]) == [1, 4]

    def test_given_3(self):
        assert make_ends([7, 4, 6, 2]) == [7, 2]
