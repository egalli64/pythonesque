"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
middle_way: https://codingbat.com/prob/p171011
"""
from middle_way import middle_way


class TestMiddleWay:
    """assuming pytest"""

    def test_given_1(self):
        assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]

    def test_given_2(self):
        assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]

    def test_given_3(self):
        assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
