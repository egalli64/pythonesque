"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
array_front9 https://codingbat.com/prob/p110166
"""
from array_front9 import array_front9, array_front9_no_slice


class TestArrayFront9:
    def test_given_1(self):
        assert array_front9([1, 2, 9, 3, 4]) is True

    def test_given_2(self):
        assert array_front9([1, 2, 3, 4, 9]) is False

    def test_given_3(self):
        assert array_front9([1, 2, 3, 4, 5]) is False

    def test_given_no_slice_1(self):
        assert array_front9_no_slice([1, 2, 9, 3, 4]) is True

    def test_given_no_slice_2(self):
        assert array_front9_no_slice([1, 2, 3, 4, 9]) is False

    def test_given_no_slice_3(self):
        assert array_front9_no_slice([1, 2, 3, 4, 5]) is False
