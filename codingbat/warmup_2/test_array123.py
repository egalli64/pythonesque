"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
array123 https://codingbat.com/prob/p193604
"""
from array123 import array123, array123_any


class TestArray123:
    def test_given_1(self):
        assert array123([1, 1, 2, 3, 1]) is True

    def test_given_2(self):
        assert array123([1, 1, 2, 4, 1]) is False

    def test_given_3(self):
        assert array123([1, 1, 2, 1, 2, 3]) is True

    def test_given_any_1(self):
        assert array123_any([1, 1, 2, 3, 1]) is True

    def test_given_any_2(self):
        assert array123_any([1, 1, 2, 4, 1]) is False

    def test_given_any_3(self):
        assert array123_any([1, 1, 2, 1, 2, 3]) is True
