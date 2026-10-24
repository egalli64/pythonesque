"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
big_diff: https://codingbat.com/prob/p184853
"""
import pytest
from big_diff import big_diff


class TestCountEvens:
    def test_given_1(self):
        assert big_diff([10, 3, 5, 6]) == 7

    def test_given_2(self):
        assert big_diff([7, 2, 10, 9]) == 8

    def test_given_3(self):
        assert big_diff([2, 10, 7, 2]) == 8

    def test_single(self):
        assert big_diff([42]) == 0

    def test_empty(self):
        with pytest.raises(ValueError):
            big_diff([])

    def test_none(self):
        # noinspection PyTypeChecker
        pytest.raises(TypeError, big_diff, None)
