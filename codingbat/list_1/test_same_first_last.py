"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
same_first_last: https://codingbat.com/prob/p179078
"""
from same_first_last import same_first_last


class TestSameFirstLast:
    """assuming pytest"""

    def test_given_1(self):
        assert same_first_last([1, 2, 3]) is False

    def test_given_2(self):
        assert same_first_last([1, 2, 3, 1]) is True

    def test_given_3(self):
        assert same_first_last([1, 2, 1]) is True

    def test_empty(self):
        assert same_first_last([]) is False
