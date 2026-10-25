"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
has22: https://codingbat.com/prob/p119308
"""
from has22 import has22, has22_modern, has22_zip


class TestHas22:
    def test_given_1(self):
        assert has22([1, 2, 2]) is True

    def test_given_2(self):
        assert has22([1, 2, 1, 2]) is False

    def test_given_3(self):
        assert has22([2, 1, 2]) is False


class TestHas22Zip:
    def test_given_1(self):
        assert has22_zip([1, 2, 2]) is True

    def test_given_2(self):
        assert has22_zip([1, 2, 1, 2]) is False

    def test_given_3(self):
        assert has22_zip([2, 1, 2]) is False


class TestHas22Modern:
    def test_given_1(self):
        assert has22_modern([1, 2, 2]) is True

    def test_given_2(self):
        assert has22_modern([1, 2, 1, 2]) is False

    def test_given_3(self):
        assert has22_modern([2, 1, 2]) is False
